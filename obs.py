import obspython as obs
import time
import threading

# Configuração
PRIMARY_MONITOR_SCENE = "Monitor 1"
SECONDARY_MONITOR_SCENE = "Monitor 2"
MONITOR_WIDTH = 0

class MouseMonitor:
    def __init__(self):
        self.running = False
        self.thread = None
        self.last_monitor = 1
        self.paused = False  # Nova variável para o kill switch
        self.caps_lock_state = False  # Estado atual do Caps Lock

    def is_caps_lock_on(self):
        """Verifica se o Caps Lock está ativo"""
        try:
            import ctypes
            return ctypes.windll.user32.GetKeyState(0x14) & 1 != 0
        except:
            return False
    
    def get_current_monitor(self):
        """Detecta qual monitor baseado na posição X do mouse"""
        try:
            import ctypes
            
            class POINT(ctypes.Structure):
                _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
            
            pt = POINT()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
            
            # Monitor 1: x < largura_do_monitor, Monitor 2: x >= largura_do_monitor
            return 1 if pt.x < MONITOR_WIDTH else 2
            
        except:
            return 1
    
    def switch_scene(self, monitor_num):
        """Troca para a cena do monitor especificado"""
        scene_name = PRIMARY_MONITOR_SCENE if monitor_num == 1 else SECONDARY_MONITOR_SCENE
        
        scenes = obs.obs_frontend_get_scenes()
        for scene in scenes:
            if obs.obs_source_get_name(scene) == scene_name:
                obs.obs_frontend_set_current_scene(scene)
                print(f"Trocado para: {scene_name}")
                break
        obs.source_list_release(scenes)
    
    def monitor_loop(self):
        """Loop principal de monitoramento"""
        while self.running:
            # Verificar se o Caps Lock foi pressionado (kill switch)
            current_caps_state = self.is_caps_lock_on()
            
            # Se o estado do Caps Lock mudou
            if current_caps_state != self.caps_lock_state:
                self.caps_lock_state = current_caps_state
                self.paused = current_caps_state  # Pausar quando Caps Lock estiver ON
                
                if self.paused:
                    print("PAUSADO (Caps Lock ATIVO)")
                else:
                    print("RETOMADO (Caps Lock DESATIVADO)")
            
            # Só troca de cena se não estiver pausado
            if not self.paused:
                current_monitor = self.get_current_monitor()
                
                if current_monitor != self.last_monitor:
                    self.switch_scene(current_monitor)
                    self.last_monitor = current_monitor
            
            time.sleep(0.3)  # Verifica a cada 300ms
    
    def start(self):
        """Inicia o monitoramento"""
        if self.running:
            return
        
        # Verificar estado inicial do Caps Lock
        self.caps_lock_state = self.is_caps_lock_on()
        self.paused = self.caps_lock_state
        
        if self.paused:
            print("Monitoramento em modo PAUSE (Caps Lock ATIVO)")
        else:
            print("Monitoramento iniciado")
        
        self.running = True
        self.thread = threading.Thread(target=self.monitor_loop)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        """Para o monitoramento"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2.0)
        print("Monitoramento do mouse parado")

# Instância global
mouse_monitor = MouseMonitor()

def script_description():
    return "Troca entre monitores automaticamente baseado na posição do mouse mude o nome das cenas 'Monitor 1' e 'Monitor 2'. Use Caps Lock para PAUSAR/RETOMAR."

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "info_details", "Ajuste Manual da Largura do Monitor 1", obs.OBS_TEXT_INFO)
    obs.obs_properties_add_int(props, "monitor_width", "Largura 1", 0, 3840, 1)

    obs.obs_properties_add_text(props, "info2", "", obs.OBS_TEXT_INFO)

    obs.obs_properties_add_text(props, "primary_scene", "Cena Monitor 1", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "secondary_scene", "Cena Monitor 2", obs.OBS_TEXT_DEFAULT)

    obs.obs_properties_add_text(props, "info3", "", obs.OBS_TEXT_INFO)

    obs.obs_properties_add_text(props, "info4", "Loop de Detecção", obs.OBS_TEXT_INFO)

    obs.obs_properties_add_button(props, "start_btn", "Iniciar", start_script)
    obs.obs_properties_add_button(props, "stop_btn", "Parar", stop_script)

    obs.obs_properties_add_text(props, "info5", "", obs.OBS_TEXT_INFO)

    obs.obs_properties_add_text(props, "info6", "", obs.OBS_TEXT_INFO)

    obs.obs_properties_add_text(props, "info7", "Desenvolvedor: @enricomalta", obs.OBS_TEXT_INFO)

    return props

def script_defaults(settings):
    """Define os valores padrão quando o script é carregado pela primeira vez"""
    obs.obs_data_set_string(settings, "primary_scene", "Monitor 1")
    obs.obs_data_set_string(settings, "secondary_scene", "Monitor 2")
    obs.obs_data_set_int(settings, "monitor_width", 0)

def script_update(settings):
    global PRIMARY_MONITOR_SCENE, SECONDARY_MONITOR_SCENE, MONITOR_WIDTH
    PRIMARY_MONITOR_SCENE = obs.obs_data_get_string(settings, "primary_scene")
    SECONDARY_MONITOR_SCENE = obs.obs_data_get_string(settings, "secondary_scene")
    MONITOR_WIDTH = obs.obs_data_get_int(settings, "monitor_width")

def start_script(props, prop):
    mouse_monitor.start()
    return True

def stop_script(props, prop):
    mouse_monitor.stop()
    return True

def script_unload():
    mouse_monitor.stop()
# OBS Mouse Monitor Switcher

Script Python para OBS Studio que troca automaticamente entre cenas de monitor baseado na posição do mouse, com função de pausa via Caps Lock.

## 🚀 Desenvolvido por **@enricomalta**

## 📋 Funcionalidades

- **Troca automática** entre monitores baseado na posição do mouse
- **Kill Switch com Caps Lock** - pausa/retoma o monitoramento instantaneamente
- **Configuração simples** via interface do OBS
- **Detecção precisa** de múltiplos monitores

## 🛠️ Instalação

1. **Abra o OBS Studio**
2. Vá em **Ferramentas → Scripts**
3. Clique no **+** (Adicionar) 
4. Selecione o arquivo `obs.py`
5. Configure as opções conforme necessário
6. Clique em Configurações do Python e Explorar
7. Cole no Caminho de instalação do Python o path do seu sistema exemplo
9. EXEMPLO Usuario Joao e Python 3.10 " C:/Users/Joao/AppData/Local/Programs/Python/Python/310 "

## ⚙️ Configuração

### Parâmetros do Script:

- **Cena Monitor 1**: Nome da cena que corresponde ao primeiro monitor
- **Cena Monitor 2**: Nome da cena que corresponde ao segundo monitor  
- **Largura Monitor 1**: Deixe em 0 Caso o mouse não respeite aumente ou diminua o valor para ajustar a troca

### 📋 Pré-requisitos:

- **OBS Studio** (versão 28 ou superior)
- **Windows** (script utiliza APIs do Windows)
- **Python** 3.10+
- **Duas cenas configuradas** no OBS, cada uma capturando um monitor diferente

## 🎮 Como Usar

### Controles Básicos:
- **Iniciar**: Clique no botão "Iniciar" para começar o monitoramento
- **Parar**: Clique em "Parar" para interromper o script
- **Caps Lock**: Use como kill switch para pausar/retomar instantaneamente

### Funcionamento:
1. **Mouse no Monitor 1** → Ativa cena do Monitor 1
2. **Mouse no Monitor 2** → Ativa cena do Monitor 2  
3. **Caps Lock ATIVO** → Pausa o monitoramento (travando na cena atual)
4. **Caps Lock DESATIVADO** → Retoma o monitoramento automático

## 🔧 Solução de Problemas

### ❌ Script não detecta monitores corretamente:
- Verifique se a **largura do Monitor 1** está configurada corretamente
- Confirme se os **nomes das cenas** batem exatamente com os do OBS

### ❌ Caps Lock não funciona:
- Certifique-se de que o **teclado está funcionando** normalmente
- Verifique se há **outros scripts** conflitantes

### ❌ Script não inicia:
- **Reinicie o OBS** e recarregue o script
- Verifique se há **erros no console** do OBS

## 💡 Dicas de Uso

### Para Transmissões:
- Use o **Caps Lock** quando precisar focar em um monitor específico
- Ideal para **tutoriais** onde você alterna entre código e apresentação
- Perfeito para **suporte técnico** mostrando diferentes telas

### Para Gravações:
- Configure **atalhos de teclado** no OBS para iniciar/parar rapidamente
- Use em conjunto com **transições personalizadas** para efeitos suaves

## 📄 Licença

Este script é disponibilizado gratuitamente para uso pessoal e profissional. Desenvolvido por **@enricomalta**.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades  
- Enviar pull requests

## 📞 Suporte

Em caso de problemas ou dúvidas:
1. Verifique a **seção de solução de problemas** acima
2. Confirme se **todas as dependências** estão instaladas
3. Teste com **configurações mínimas** primeiro

---

**Desenvolvido com ❤️ por @enricomalta para a comunidade OBS**

# Job Event Listener Notificator

**Índice**
1. [Introdução](#intr)
2. [Configuração de ambiente](#cs1)
3. [Rodar projeto](#run)


## Introdução <a name="intr"></a>

Esse serviço é responsável por receber eventos de atualização dos status dos jobs e fazer a atualização dos mesmos no banco e notificar a uma lista de e-mails.
A notificação a priori funciona somente para gmail.

O arquivo `settings.py` é responsável por capturar as variáveis de ambiente requeridas para o projeto.


## Configuração de ambiente <a name="cs1"></a>
Instalar dependências(rodar na raíz do projeto, versão do Python é 3.7)
````bash
pip install -r requirements.txt
````

## Rodar Projeto <a name="run"></a>
Comando para iniciar aplicação
````bash
python main.py
````


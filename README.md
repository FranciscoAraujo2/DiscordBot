# DiscordBot
🤖・Discord Bot

# Disnake 
* pip install disnake <br>
* https://docs.disnake.dev/en/latest/

# Cogs

```py
extensions = []
directory = 'cogs'
for file in os.listdir(directory):
    if file.endswith('.py'):
        extensions.append(f'{directory}.{file[:-3]}')

for extension in extensions:
    bot.load_extension(extension)
    print(f'{extension} loaded!')
```


| Systems | Description |
| --- | --- |
| Economy | Lista de todos os arquivos modificados ou novos |
| Moderation | Mostra as diferenças do arquivo que não foram preparadas |
| Fun | Mostra as diferenças do arquivo que não foram preparadas |

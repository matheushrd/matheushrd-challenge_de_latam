# Define as variáveis de ambiente para o usuário atual
[Environment]::SetEnvironmentVariable("FILE_ID", "1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("CREDS_PATH", "./creds.json", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("FILENAME", "tweets", [EnvironmentVariableTarget]::User)

# Exibe uma mensagem indicando que as variáveis foram definidas
Write-Host "Variáveis de ambiente definidas."

# Pausa o script para que a janela do PowerShell não feche imediatamente
Read-Host -Prompt "Pressione Enter para continuar..."

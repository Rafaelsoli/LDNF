@echo off
setlocal
set VENV_NAME=venv

:: 1. Remover a venv existente se ela existir
if exist %VENV_NAME% (
    echo [1/4] Removendo venv antiga...
    rmdir /s /q %VENV_NAME%
)

:: 2. Criar a nova venv
echo [2/4] Criando novo ambiente virtual...
python -m venv %VENV_NAME%

:: 3. Instalar requirements (se o arquivo existir)
if exist requirements.txt (
    echo [3/4] Instalando dependencias...
    %VENV_NAME%\Scripts\pip install -r requirements.txt
) else (
    echo [!] requirements.txt nao encontrado. Pulando instalacao.
)

:: 4. Adicionar ao .gitignore se nao estiver la
echo [4/4] Verificando .gitignore...
if exist .git (
    findstr /x "%VENV_NAME%/" .gitignore >nul 2>&1
    if errorlevel 1 (
        echo %VENV_NAME%/ >> .gitignore
        echo [+] %VENV_NAME%/ adicionado ao .gitignore.
    ) else (
        echo [ok] %VENV_NAME%/ ja esta no .gitignore.
    )
) else (
    echo [!] Repositorio Git nao detectado. Pulando .gitignore.
)

echo.
echo === Processo Concluido! ===
pause
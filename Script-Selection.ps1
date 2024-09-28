# Check if Python is installed
if (-not (Get-Command python3 -ErrorAction SilentlyContinue)) {
    Write-Host "Python3 is not installed." -ForegroundColor Red
    exit 1
} 
else {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        python3 --version
    } else {
        python --version
    }
    Write-Host ""
}

# Change Directory to the current script location
Set-Location -Path "./src"

# Open and execute the Python Script in the same window, wait for it to finish
Start-Process -FilePath "python" -ArgumentList "./Script-Selection.py" -NoNewWindow -Wait
Set-Location -Path ".."

# Pause for 1 second
Start-Sleep -Seconds 1

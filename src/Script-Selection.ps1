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


# Open and execute the Python Script in the same window, wait for it to finish
Start-Process -FilePath "python" -ArgumentList "./Script-Selection.py" -NoNewWindow -Wait

# Pause for 1 second
Start-Sleep -Seconds 1

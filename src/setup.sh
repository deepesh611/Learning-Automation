#!/bin/bash

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color


# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo -e "${CYAN}Python3${RED} is not installed.${NC}"
    echo "Please install python3 before proceeding."
    sleep 5
    exit 1
else
    if ! python --version &>/dev/null; then
        python3 --version
    else
        python --version
    fi
    echo ""
fi

# Check if pip is installed
if ! command -v pip &>/dev/null; then
    echo -e "${CYAN}pip${RED} is not installed.${NC}"
    echo "Please install pip before proceeding."
    sleep 5
    exit 1
else
    pip --version
    echo ""
fi


# Start pip installation for any additional requirements
if [ -f requirements.txt ]; then
    if pip install -r requirements.txt; then
        echo -e "${GREEN}\nModules installed Successfully...${NC}"
    else
        echo -e "${RED}\nFailed to install modules.${NC}"
        sleep 5
        exit 1
    fi
fi

sleep 1    
echo -e "${GREEN}\nSetup Completed Successfully...${NC}"
sleep 1
echo -e "${PURPLE}\nPress Enter to continue...${NC}"

read -r

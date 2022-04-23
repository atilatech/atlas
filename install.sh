pip install virtualenv

if [ ! -d "venv" ]; then
    virtualenv venv --python=python3
fi

if [ ! -f ".env" ]; then
    cp shared.env .env
fi

source venv/bin/activate
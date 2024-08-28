from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """
        funcao teste
    """
    return {'message': 'Olá Mundo!'}

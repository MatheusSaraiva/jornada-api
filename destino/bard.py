import os

from bardapi import Bard

os.environ['_BARD_API_KEY'] = "Ywhf86hwRpRaa5jTz4DJQOEO3De4gwlrDG0OqkgxVgklpMLEF_pNqHQaRGUdAZuTRVGySQ."


def bard_descritivo(nome):
    input_text = f"Faça um resumo sobre {nome} enfatizando o porque este lugar é incrível.\
      Utilize uma linguagem informal e até 100 caracteres no máximo em cada parágrafo.\
          Crie 2 parágrafos neste resumo."
    
    bard_output = Bard().get_answer(input_text)['content']
    return bard_output
# Computer_Vision_Learn
Repositório com a finalidade de estudar Visão Computacional com Python e OpenCV

### Pré Requisitos

Artigo no Medium para apoio na preparação do ambiente:
- [Como instalar dlib para Python](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f)

Para a analise e classificação de faces é necessário a instalação do OpenCV, Dlib e CMake.

O CMake é uma dependência necessária para o Dlib (pois foi desenvolvido em linguagem C), esta biblioteca contem alguns classificadores pré treinados que conseguem reconhecer partes do rosto, como queixo, nariz, olhos, etc. 
- https://cmake.org/download/

Instalar o cmake no ambiente Python:
```bash
    pip install cmake
```

Instalar dlib:
```bash
    pip install dlib
```

Instalar OpenCV:
```bash
    pip install opencv-python
```

### Curiosidades

Vídeo sobre a diferença de *Classificação de Imagens*, *Detecção de Objetos* e *Segmentação*.
- [A Base da Visão Computacional](https://www.youtube.com/watch?v=6nOpw6XqgwI)
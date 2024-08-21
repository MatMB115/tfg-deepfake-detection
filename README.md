<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/MatMB115/TFG-UNIFEI-scope-review-about-deepfakes-detection?color=a015f5">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/MatMB115/TFG-UNIFEI-scope-review-about-deepfakes-detection">

  <a href="https://github.com/MatMB115/TFG-UNIFEI-scope-review-about-deepfakes-detection/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/MatMB115/TFG-UNIFEI-scope-review-about-deepfakes-detection">
  </a>
  
<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
  <a href="https://github.com/MatMB115/rTFG-UNIFEI-scope-review-about-deepfakes-detection/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/MatMB115/TFG-UNIFEI-scope-review-about-deepfakes-detection?style=social">
  </a>
</p>


# Revisão da Literatura Sobre Detecção de Deepfake

Este repositório é uma fonte central de informações sobre a revisão da literatura sobre **Detecção de Deepfake**. Aqui, você encontrará uma compilação de recursos, incluindo artigos, relatórios e modelos de outros repositórios relevantes. O objetivo é fornecer uma referência única e acessível para pesquisadores e profissionais interessados na detecção de deepfakes e viabilizar a realização do TFG para graduação na Universidade Federal de Itajubá.


## Guia das Seções
- [Revisão da Literatura Sobre Detecção de Deepfake](#revisão-da-literatura-sobre-detecção-de-deepfake)
  - [Guia das Seções](#guia-das-seções)
  - [Ferramentas](#ferramentas)
    - [DeepfakeLab](#deepfakelab)
    - [Face-recognicion](#face-recognicion)
    - [MediaPipe](#mediapipe)
    - [DeepFace](#deepface)
    - [Keras](#keras)
  - [Material Analisado](#material-analisado)
    - [Repositório de Compilado de Tecnologias de Deepfake](#repositório-de-compilado-de-tecnologias-de-deepfake)
    - [Benchmarks](#benchmarks)
    - [Modelos](#modelos)
    - [Datasets](#datasets)
      - [FaceForensics++](#faceforensics)
      - [DeepfakeTIMIT](#deepfaketimit)
  - [Sobre mim](#sobre-mim)

## Ferramentas

https://github.com/topics/deepfakes

### DeepfakeLab

O DeepFaceLab é um software usado para criar deepfakes, especialmente para troca de rostos. Ele foi desenvolvido para ser fácil de usar, oferecendo ferramentas poderosas para criar deepfakes de alta qualidade.
- article: [DeepFaceLab: Integrated, flexible and extensible face-swapping framework](https://arxiv.org/abs/2005.05535)
- repo: [DeepFaceLab](https://github.com/iperov/DeepFaceLab?tab=readme-ov-file)

Encontrei uma tentativa de rodar uma versão limitado do DFL com um colab:
- https://github.com/dream80/DeepFaceLab_Colab

### Face-recognicion
Reconheça e manipule rostos em Python ou na linha de comando com a biblioteca de reconhecimento facial mais simples do mundo. Utilizado como backend na maioria dos modelos que faz análise da face.
- repo: https://github.com/ageitgey/face_recognition

### MediaPipe
MediaPipe Solutions fornece um conjunto de bibliotecas e ferramentas para você aplicar rapidamente técnicas de inteligência artificial (IA) e aprendizado de máquina (ML) em seus aplicativos.
- repo: https://github.com/google-ai-edge/mediapipe

### DeepFace
<img src="https://imgur.com/QHfCH0l.jpg)" width="600"/>

Deepface é uma estrutura leve de reconhecimento facial e análise de atributos faciais (idade, gênero, emoção e raça) para python. Envolve modelos de última geração: VGG-Face, FaceNet, OpenFace, DeepFace, DeepID, ArcFace, Dlib, SFace e GhostFaceNet.
- repo: https://github.com/serengil/deepface

### Keras
Keras Applications are deep learning models that are made available alongside pre-trained weights. These models can be used for prediction, feature extraction, and fine-tuning.
- https://keras.io/api/applications/
- https://www.kaggle.com/c/deepfake-detection-challenge/overview

## Material Analisado
Compilado de informações que podem ser pertinentes para esse projeto.

### Repositório de Compilado de Tecnologias de Deepfake

- https://github.com/naveed88375/AI-ML
- https://github.com/datamllab/awesome-deepfakes-materials
- https://github.com/enochkan/awesome-gans-and-deepfakes
- https://github.com/aerophile/awesome-deepfakes
- https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection

### Benchmarks
- https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection

### Modelos
- https://github.com/HongguLiu/Deepfake-Detection - Funcional com modelo já treinado (3 modelos) e base é o Faceforensis++;
- https://github.com/erprogs/GenConViT -  Funcional com dois modelos (Encoder/Decoder e VAE) já treinados;
- https://github.com/polimi-ispl/icpr2020dfdc - modelo mais simples combinando CNNs, há modelos treinados para teste;
- https://github.com/skrantidatta/LIPINC - modelo baseado em inconsistência labiais para detectar deepfakes, ainda não testado;

  
### Datasets
- https://github.com/Daisy-Zhang/Awesome-Deepfakes
- https://github.com/EndlessSora/DeeperForensics-1.0
#### FaceForensics++
[FaceForensics++](https://github.com/ondyari/FaceForensics) é um conjunto de dados forenses composto por 1000 sequências de vídeo originais que foram manipuladas com quatro métodos automatizados de manipulação facial: Deepfakes, Face2Face, FaceSwap e NeuralTextures. Os dados foram obtidos de 977 vídeos do YouTube, todos contendo rostos predominantemente frontais e sem obstruções, permitindo que os métodos automatizados criem falsificações realistas. Além disso, o conjunto de dados inclui máscaras binárias, permitindo seu uso tanto para classificação de imagens e vídeos quanto para segmentação. Também são fornecidos 1000 modelos Deepfakes para gerar e aumentar novos dados.
#### DeepfakeTIMIT
[DeepfakeTIMIT](https://zenodo.org/records/4068245) é um banco de dados de vídeos onde rostos foram trocados usando uma abordagem baseada em GAN de código aberto. O banco de dados foi criado a partir de 16 pares de pessoas com aparências semelhantes selecionadas do VidTIMIT, um banco de dados público. Foram treinados dois modelos diferentes para cada um dos 32 indivíduos: um de qualidade inferior (64 x 64 pixels) e outro de qualidade superior (128 x 128 pixels). Com 10 vídeos por pessoa no VidTIMIT, foram gerados 320 vídeos para cada versão, totalizando 620 vídeos com rostos trocados. O áudio original dos vídeos foi mantido sem manipulações.

## Sobre mim

<table>
  <tr>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115/" title="RepiMe">:technologist:</a></td>
    
  </tr>
  
</table>

Olá! Sou um estudante de Ciência da Computação na Universidade Federal de Itajubá, com foco em estudar redes neurais profundas. Tenho experiência com algumas tecnologias que estão listadas no meu [perfil](https://github.com/MatMB115).
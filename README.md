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
    - [Repositório com Compilados de Publicações](#repositório-com-compilados-de-publicações)
    - [Modelos](#modelos)
    - [Datasets](#datasets)
  - [Sobre mim](#sobre-mim)

## Ferramentas

https://github.com/topics/deepfakes

### DeepfakeLab

O DeepFaceLab é um software usado para criar deepfakes, especialmente para troca de rostos. Ele foi desenvolvido para ser fácil de usar, oferecendo ferramentas poderosas para criar deepfakes de alta qualidade.
- paper: [DeepFaceLab: Integrated, flexible and extensible face-swapping framework](https://arxiv.org/abs/2005.05535)
- repo: [DeepFaceLab](https://github.com/iperov/DeepFaceLab?tab=readme-ov-file)
- colab: https://github.com/dream80/DeepFaceLab_Colab

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

### Repositório com Compilados de Publicações
- https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection - Abrangente
- https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection - Direcionado
- https://github.com/SCLBD/DeepfakeBench - Benchmark feito com 15 modelos (estado da arte) e 9 datasets (6 pós-processamento)

### Modelos
| Repositório                                                    | Backbone / Arquitetura                          | Descrição                                                                                                                   | Links Relevantes                                                                                                                                                     |
|----------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XceptionNet](https://github.com/HongguLiu/Deepfake-Detection) | XceptionNet                                    | Utiliza XceptionNet para detectar deepfakes, focando na extração de características de imagens. Treinado com FaceForensics++. | [GitHub](https://github.com/HongguLiu/Deepfake-Detection)                                                                                                           |
| [GenConViT](https://github.com/erprogs/GenConViT)              | ConvNext, SwinTransformer                      | Modelos baseados em Autoencoder e VAE com backbones ConvNext e SwinTransformer, voltados para análise de vídeo.              | [GitHub](https://github.com/erprogs/GenConViT)                                                                                                                     |
| [icpr2020dfdc](https://github.com/polimi-ispl/icpr2020dfdc)    | CNNs                                           | Combina diferentes CNNs para detecção de deepfakes, com diversos modelos pré-treinados disponíveis para teste.               | [GitHub](https://github.com/polimi-ispl/icpr2020dfdc)                                                                                                              |
| [LIPINC](https://github.com/skrantidatta/LIPINC)               | MSTIE (Mouth Spatial-Temporal Inconsistency Extractor)                                | Detecta deepfakes de sincronização labial ao identificar inconsistências temporais nos movimentos labiais entre frames.       | [GitHub](https://github.com/skrantidatta/LIPINC)                                                                                                                    |
| [LipFD](https://github.com/AaronComo/LipFD)                    | ViT-L/14 (Vision Transformer)                  | Foca na detecção de deepfakes de sincronização labial, usando inconsistências temporais entre áudio e vídeo.                 | [GitHub](https://github.com/AaronComo/LipFD)                                                                                                                       |

### Datasets

| Dataset          | Ano  | Paper                                                                                                              | Download Link                                                                                                    |
|------------------|------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Deepfake-TIMIT   | 2018 | [paper](https://arxiv.org/abs/2408.05366)                                                                           | [download](https://huggingface.co/datasets/faridlab/deepspeak_v1)                                                |
| Celeb-DF (v1 & v2)| 2019 | [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Li_Celeb-DF_A_Large-Scale_Challenging_Dataset_for_DeepFake_Forensics_CVPR_2020_paper.pdf)| [download](https://github.com/yuezunli/celeb-deepfakeforensics/tree/master/Celeb-DF-v2)                         |
| FaceForensic++   | 2019 | [paper](https://arxiv.org/abs/1901.08971)                                                                           | [download](https://github.com/ondyari/FaceForensics)                                                             |
| DFDC             | 2019 | [paper](https://arxiv.org/abs/2006.07397)                                                                           | [download](https://www.kaggle.com/c/deepfake-detection-challenge/data)                                            |
| DFFD             | 2019 | [paper](http://cvlab.cse.msu.edu/pdfs/dang_liu_stehouwer_liu_jain_cvpr2020.pdf)                                     | [download](http://cvlab.cse.msu.edu/dffd-dataset.html)                                                           |
| FakeAVCeleb      | 2021 | [paper](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/d9d4f495e875a2e075a1a4a6e1b9770f-Paper-round2.pdf)| [download](https://github.com/DASH-Lab/FakeAVCeleb)                                                              |
| ***WildDeepfake***| 2021 | [paper](https://arxiv.org/abs/2101.01456)                                                                           | [download](https://github.com/deepfakeinthewild/deepfake-in-the-wild)                                             |
| ***DeepSpeak***   | 2024 | [paper](https://arxiv.org/abs/2408.05366)                                                                           | [download](https://huggingface.co/datasets/faridlab/deepspeak_v1)                                                |


## Sobre mim

<table>
  <tr>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115/" title="RepiMe">:technologist:</a></td>
    
  </tr>
  
</table>

Olá! Sou um estudante de Ciência da Computação na Universidade Federal de Itajubá, com foco em estudar redes neurais profundas. Tenho experiência com algumas tecnologias que estão listadas no meu [perfil](https://github.com/MatMB115).
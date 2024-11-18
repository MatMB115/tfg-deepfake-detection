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


# Análise Comparativa de Modelos para Detecção de Deepfake

Este repositório é uma fonte central de informações sobre o trabalho desenvolvido acerca da comparação de desempenho de novos modelos para **Detecção de Deepfake**. Aqui, você encontrará uma compilação de recursos, incluindo artigos, relatórios, modelos relevantes e scripts de pré-processamento. O objetivo é fornecer uma referência única e acessível aos interessados no trabalho desenvolvido na área de detecção de deepfakes e viabilizar a realização do Trabalho Final de Graduação (TFG) para graduação na Universidade Federal de Itajubá.


## Guia das Seções
- [Análise Comparativa de Modelos para Detecção de Deepfake](#análise-comparativa-de-modelos-para-detecção-de-deepfake)
  - [Guia das Seções](#guia-das-seções)
  - [Estrutura do Trabalho](#estrutura-do-trabalho)
  - [Ferramentas](#ferramentas)
    - [DeepfakeLab](#deepfakelab)
    - [Face-recognicion](#face-recognicion)
    - [MediaPipe](#mediapipe)
    - [DeepFace](#deepface)
    - [Keras](#keras)
  - [Material Analisado](#material-analisado)
    - [Repositório com Compilados de Publicações](#repositório-com-compilados-de-publicações)
    - [Modelos Promissores](#modelos-promissores)
    - [Datasets](#datasets)
  - [Requisitos](#requisitos)
  - [Pré-processamento](#pré-processamento)
  - [Ramificações](#ramificações)
  - [Resultados](#resultados)
  - [Sobre mim](#sobre-mim)


## Estrutura do Trabalho

    root/
    ├── .gitignore                
    ├── LICENSE                   
    ├── README.md                 # Documentação do projeto
    ├── preprocessing/            # Scripts de pré-processamento
    │   ├── deepspeak/            # Scripts específicos para o dataset DeepSpeak
    │   │   ├── create_batches.sh # Script para dividir vídeos em lotes
    │   │   ├── preprocessing.py  # Script principal de pré-processamento do DeepSpeak
    │   │   ├── sort_files.py     # Script para copiar arquivos selecionados (quantidade de frames)
    │   │   ├── dataset.py        # Baixar os dados do dataset
    │   └── mouth/                # Scripts para extração de bocas de vídeos (abordagem desconsiderada ao decorrer do trabalho)
    │   │   ├── mouth_extrator.py 
    │   │   ├── run.sh            
    │   │   └── split_videos.bash 
    │   └── wild_deepfake/        # Scripts específicos para o dataset WildDeepfake
    │       ├── extract.py        # Script para copiar, reorganizar imagens e gerar metadados (json)
    │       └── sort.py           # Script para copiar arquivos
    ├── requirements.txt          # Dependências do projeto
    └── result/                   # Resultados das predições em JSON e binário
    │   ├── assets/               # Gráficos e tabelas gerados    
    │   ├── original/             
    │   ├── original_benchmark/   
    │   ├── retrain/              
    │   ├── retrain_benchmark/    
    └── result_all.py         # Script para processar e analisar todos os resultados

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

## Material Analisado
Compilado de informações pertinentes para esse trabalho.

### Repositório com Compilados de Publicações
- https://github.com/flyingby/Awesome-Deepfake-Generation-and-Detection - Abrangente
- https://github.com/Daisy-Zhang/Awesome-Deepfakes-Detection - Direcionado
- https://github.com/SCLBD/DeepfakeBench - Benchmark feito com 15 modelos (estado da arte) e 9 datasets (resultando em 6 pós-processamento)

### Modelos Promissores
| Status | Repositório                                                    | Backbone                                               | Descrição                                                                                                                                                                                                                            | Fonte                                                                                                    |  Implementação    |
|--------|----------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------|
| ✅      | [XceptionNet](https://github.com/HongguLiu/Deepfake-Detection) | Xception                                               | Utiliza XceptionNet para detectar deepfakes, focando na extração de características de imagens. Treinado com FaceForensics++.                                                                                                        | [GitHub](https://github.com/SCLBD/DeepfakeBench/blob/main/training/detectors/xception_detector.py)       | DeepfakeBenchmark |
| ✅      | [GenConViT](https://github.com/erprogs/GenConViT)              | ConvNext, SwinTransformer                              | Modelos baseados em Autoencoder e VAE com backbones ConvNext e SwinTransformer, voltados para análise de vídeo.                                                                                                                      | [GitHub](https://github.com/erprogs/GenConViT)                                                           | Original          |
| ⭕      | [icpr2020dfdc](https://github.com/polimi-ispl/icpr2020dfdc)    | CNNs                                                   | Combina diferentes CNNs para detecção de deepfakes, com diversos modelos pré-treinados disponíveis para teste.                                                                                                                       | [GitHub](https://github.com/polimi-ispl/icpr2020dfdc)                                                    | Original          |
| ⭕      | [LIPINC](https://github.com/skrantidatta/LIPINC)               | MSTIE (Mouth Spatial-Temporal Inconsistency Extractor) | Detecta deepfakes de sincronização labial ao identificar inconsistências temporais nos movimentos labiais entre frames utilizando mecanismo de atenção.                                                                                                              | [GitHub](https://github.com/skrantidatta/LIPINC)                                                         | Original          |
| ⭕      | [LipFD](https://github.com/AaronComo/LipFD)                    | ViT-L/14 (Vision Transformer)                          | Foca na detecção de deepfakes de sincronização labial, usando inconsistências temporais entre áudio e vídeo.                                                                                                                         | [GitHub](https://github.com/AaronComo/LipFD)                                                             | Original          |
| ✅      | [SPSL](https://arxiv.org/abs/2103.01856)                       | Xception                                               | Combina informações espaciais e do espectro de fase para detectar artefatos de up-sampling em imagens forjadas, focando em texturas locais ao reduzir a profundidade da rede para melhorar a detecção de deepfakes.                  | [GitHub](https://github.com/SCLBD/DeepfakeBench/blob/main/training/detectors/spsl_detector.py)           | DeepfakeBenchmark |
| ✅      | [UCF](https://arxiv.org/abs/2304.13949)                        | Xception                                               | Decompõe a imagem em componentes irrelevantes à falsificação, específicos ao método de falsificação e comuns a várias falsificações, utilizando apenas os componentes comuns para melhorar a generalização na detecção de deepfakes. |  [GitHub](https://github.com/SCLBD/DeepfakeBench/blob/main/training/detectors/ucf_detector.py)           | DeepfakeBenchmark |
| ✅      | [EfficientB4](https://arxiv.org/abs/1905.11946)                | EfficientB4                                            | Escala de maneira uniforme a profundidade, largura e resolução da rede usando um coeficiente composto, otimizando o desempenho e a eficiência através de uma arquitetura cuidadosamente projetada e dimensionada.                    | [GitHub](https://github.com/SCLBD/DeepfakeBench/blob/main/training/detectors/efficientnetb4_detector.py) | DeepfakeBenchmark |
| ✅      | [MesoNet](https://arxiv.org/abs/1809.00888)                    | Meso4Inception                                         | Detecta falsificações faciais em vídeos analisando propriedades mesoscópicas das imagens através de redes profundas com poucas camadas, otimizadas para lidar com compressão e detectar deepfakes e Face2Face.                       | [GitHub](https://github.com/SCLBD/DeepfakeBench/blob/main/training/detectors/meso4Inception_detector.py) | DeepfakeBenchmark |
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

A figura abaixo ilustra os tipos de amostras presentes em alguns dos datasets relevantes na literatura.
![Datasets](https://imgur.com/0p6sdEH.jpg)

## Requisitos
As etapas abaixo são necessárias para reproduzir o pré-processamento ou visualizar os resultados obtidos.

1. Clone o repositório:
```bash
git clone https://github.com/MatMB115/tfg-deepfake-detection
cd tfg-deepfake-detection
```

1. Crie e ative um ambiente virtual Python:
```bash
python -m venv local
source local/bin/activate  # Para Linux/MacOS
# .\local\Scripts\Activate.ps1  # Para Windows PowerShell
# .\local\Scripts\activate  # Para Windows Command Prompt
```

1. Instale as dependências:
```bash
pip install -r requirements.txt
```
## Pré-processamento

Os scripts de pré-processamento neste repositório são destinados principalmente para o modelo GenConViT. Para os modelos do Deepfakebenchmark, foi utilizado o pipeline de pré-processamento fornecido pelo próprio benchmark. Os conjuntos de dados utilizados são o ***DeepSpeak e o WildDeepfake***. A pasta `preprocessing/` contém subpastas específicas para cada dataset. Esses scripts garantem que os dados estejam prontos para serem utilizados nos experimentos com o GenConViT.

## Ramificações
Os códigos do GenConViT e do Deepfake Benchmark foram adaptados para atender às necessidades específicas deste projeto. É possível encontrar os novos repositório em:
- [GenConViT](https://github.com/MatMB115/GenConViT_Comparative)
- [DeepfakeBench](https://github.com/MatMB115/DeepfakeBench)

As principais modificações incluem:

- Adição de suporte a novos datasets **(Ambos)**: O pipeline foi ajustado para permitir a integração e o processamento de novos conjuntos de dados, como DeepSpeak e WildDeepfake (apenas para o GenConViT).
- Implementação de ajustes para predições **(GenConViT)**: modificações para permitir a predição utilizando datasets que contêm apenas imagens pré-processadas.
- Funcionalidades para salvar dados de predição **(Ambos)**: salvar os dados de predição, permitindo uma análise posterior mais detalhada e organizada.

## Resultados
O script `result_all.py` é responsável por processar os JSONs e binários com as informações armazenadas das predições. Ao executá-lo, serão gerados os gráficos e tabelas que foram apresentados na monografia.

## Sobre mim

<table>
  <tr>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115/" title="RepiMe">:technologist:</a></td>
    
  </tr>
  
</table>

Olá! Sou um estudante de Ciência da Computação na Universidade Federal de Itajubá, com foco em estudar redes neurais profundas. Tenho experiência com algumas tecnologias que estão listadas no meu [perfil](https://github.com/MatMB115).
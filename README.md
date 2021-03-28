# SC-GlowTTS: an Efficient Zero-Shot Multi-Speaker Text-To-Speech Model
**Edresson Casanova, Christopher Shulby, Eren Gölge, Nicolas Michael Müller, Frederico Santos de Oliveira, Arnaldo Candido Junior, Anderson da Silva Soares, Sandra Maria Aluisio, Moacir Antonelli Ponti**

In our recent paper we propose SC-GlowTTS: an efficient zero-shot multi-speaker text-to-speech model that improves similarity for speakers unseen in training. We propose a speaker conditional architecture that explores a flow-based decoder that can work in a zero-shot scenario. As text encoders, we explored a dilated residual convolutional-based encoder, gated convolutional-based encoder, and transformer-based encoder. Additionally, we have shown that adjusting a GAN-based vocoder for the spectrograms predicted by the TTS model on the training dataset can significantly improve the similarity and speech quality for new speakers. We showed that our model can converge in training, using only 11 speakers, reaching state-of-the-art results for similarity with new speakers and speech quality.


## Audios samples
Visit our [website](https://edresson.github.io/SC-GlowTTS/) for audio samples.

## Implementation
All of our experiments were implemented at [Coqui TTS](https://github.com/coqui-ai/tts).

## Checkpoints

| Model                        | URL                                                                                            |
|------------------------------|------------------------------------------------------------------------------------------------|
| Speaker Encoder              | [link](https://drive.google.com/drive/folders/1LiPeThFS1mYwXb4dKCcutNgrRQxt9-H6?usp=sharing)   |
| Tacotron 2                   | [link](https://drive.google.com/drive/folders/1fwDjHJAG12Zc2SZIw309chdXlEFKMTBJ?usp=sharing)   |
| SC-GlowTTS-Trans             | [link]( https://drive.google.com/drive/folders/1YT-hxIrDQfMwVPM0bRNQqYbks7yMjC8V?usp=sharing ) |
| SC-GlowTTS-Res               | [link](  https://drive.google.com/drive/folders/1_vj4_cWGDya-AZXEe2tabSWBDXdzYDN8?usp=sharing) |
| SC-GlowTTS-Gated             | [link]( https://drive.google.com/drive/folders/1E4fim0MAi2VOjBTbRyBkRqO5lqjv4zc5?usp=sharing ) |
| SC-GlowTTS-Trans 11 speakers | [link]( https://drive.google.com/drive/folders/1B2DU2_85LUIGLBtQBwpDJvQ5k6ovuHUP?usp=sharing ) |
| HiFi-GAN                     | [link](https://drive.google.com/drive/folders/1wqGF9GoQ4rQfj58hHQ6vxW73aNmqxx89?usp=sharing  ) |
| All checkpoints                | [link](https://drive.google.com/drive/folders/15H5xB26no5DWZNbWoG6Rs04hSkdm-Q2s?usp=sharing)   |

## Colab demos

[SC-GlowTTS-Trans](https://colab.research.google.com/drive/1yyQDc-xWCqa2g-d1joW_goqbYZKaImsJ?usp=sharing)

[SC-GlowTTS-Res](https://colab.research.google.com/drive/12xhFAoIMbrAZLDl52qoCewclcWrseZvn?usp=sharing)

[SC-GlowTTS-Gated](https://colab.research.google.com/drive/12AkecRGFFgqchoSYiySjqgb-MzFp_eUo?usp=sharing)

[SC-GlowTTS-Trans trained with 11 speakers](https://colab.research.google.com/drive/12EeCCoHwTa6LePlZKy2u9NHdQJl7lrpw?usp=sharing)

## Preprocessed datasets
[VCTK Removed Silences](https://drive.google.com/drive/folders/1VEws5CYzYI3EEWwWxsDov1atIKy1luia?usp=sharing)

---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
nav_order: 1
---

<style type="text/css">
    .label {
        margin-left: 0!important;
    }

    td:first-child {
        min-width: 0;
        width: 4rem;
    }
</style>

# Introduction to Machine Learning

**University of California, Berkeley**, Fall 2023

Welcome to CS 189/289A! This class covers theoretical foundations, algorithms, methodologies, and applications for machine learning. Topics may include supervised methods for regression and classication (linear models, trees, neural networks, ensemble methods, instance-based methods); generative and discriminative probabilistic models; deep learning models including CNNs, Transformers, graph neural networks for vision and language tasks; and Markovian models for reinforcement learning and robotics.

Here are the Gradescope/Ed codes (you should self-enroll in these). We won't post any materials on bCourses.
- Gradescope: E73744
- Ed: [https://edstem.org/us/join/fCBF32](https://edstem.org/us/join/fCBF32)

Also, the Professors will post slides prior to lecture at this Google Drive [folder](https://drive.google.com/drive/u/0/folders/1eZplfXbQytcvNTK2ssLYinYSF4rJ1eWI) (for faster access). The material here is redundant with the website, but it may take up to a day or two for the website to get updated with the slides after lecture. The "Post-Lecture" subfolder contains updates to slides that the Professors may make right after lecture.

**Note:** The topics for future lectures, discussions, and HWs are tentative and may be moved around, changed, or removed.

## Overview

### Week 1

|  8/24 | <span class="label">Lecture 1</span> Introduction and Logistics  | [Slides](docs/lec1.pdf) / [Recording](https://drive.google.com/file/d/17vOI3LiRlutst2MDqfVh_FArlM19yoaM/view?usp=drive_link) |

### Week 2

|  8/28 | <span class="label label-yellow">Homework 1</span> Math Review (**Due 9/8 11:59pm**)  | [PDF](docs/hw1.pdf)  |
|  8/29 | <span class="label">Lecture 2</span> Maximum Likelihood Estimation  | [Slides](docs/lec2.pdf) / [Recording](https://drive.google.com/file/d/1GYlD4z8uGlLyyMUn2H093K6PQXDDLoOE/view?usp=drive_link) |
|  8/30 | <span class="label label-green">Discussion 0</span> Math Pre-Requisites Review  | [PDF](docs/dis0.pdf) / [Solutions](docs/dis0_sol.pdf)  |
|  8/31 | <span class="label">Lecture 3</span> Multivariate Gaussians  | [Slides](docs/lec3.pdf) / [Recording](https://drive.google.com/file/d/10EbN8y9B6n0tkSMq4dkF1yy_eIA-euvL/view?usp=drive_link) |

### Week 3

|  9/5 | <span class="label">Lecture 4</span> Linear Regression 1  | [Slides](docs/lec4.pdf) / [Recording](https://drive.google.com/file/d/1rdCmjMm5Ebctk0wWYAbLpiwGlPmB6Bbo/view?usp=drive_link) |
|  9/6 | <span class="label label-green">Discussion 1</span> MLE & Gaussians  | [PDF](docs/dis1.pdf) / [Solutions](docs/dis1_sol.pdf)  |
|  9/7 | <span class="label">Lecture 5</span> Linear Regression 2  | [Slides](docs/lec5.pdf) / [Recording](https://drive.google.com/file/d/1NgMaqYB6-UgCXY-hS8eVSyCXFCRBGtMx/view?usp=drive_link) |
|  9/9 | <span class="label label-yellow">Homework 2</span> Linear/Logistic Regression & Classification (**Due 9/22 11:59pm**)  | [PDF](docs/hw2.pdf) |

### Week 4

|  9/12 | <span class="label">Lecture 6</span> Classification - Generative & Discriminative  | [Slides](docs/lec6.pdf) / [Recording](https://drive.google.com/file/d/1gQWIiTXpdy3NnJ7O4QLcHlxxFzU__tEZ/view?usp=drive_link) |
|  9/13 | <span class="label label-green">Discussion 2</span> Linear Regression  | [PDF](docs/dis2.pdf) / [Solutions](docs/dis2_sol.pdf) |
|  9/14 | <span class="label">Lecture 7</span> Logistic Regression & Neural Networks  | [Slides](docs/lec7.pdf) / [Recording](https://drive.google.com/file/d/1TL2TWg4JQRXhEAaYKwp6PrMF0hIpe3n3/view?usp=drive_link) |

### Week 5

|  9/19 | <span class="label">Lecture 8</span> Backpropagation and Gradient Descent 1  | [Slides](docs/lec8.pdf) / [Recording](https://drive.google.com/file/d/1sT6bAbzoQ9srI3vuTSDXczFpsEjfGhf4/view?usp=drive_link) |
|  9/20 | <span class="label label-green">Discussion 3</span> Classification & Logistic Regression  | [PDF](docs/dis3.pdf) / [Solutions](docs/dis3_sol.pdf) / [Walkthrough](https://drive.google.com/file/d/1HJ5wUWDDbewZFB09vSj3qkY4GmsW8zRO/view?usp=share_link) |
|  9/21 | <span class="label">Lecture 9</span> Backpropagation and Gradient Descent 2  | [Handout](docs/lec9.pdf) / [Recording](https://drive.google.com/file/d/1omrhDd-wi2cYAvImr7lYJG0AOB9MGqTS/view?usp=drive_link) |
|  9/23 | <span class="label label-yellow">Homework 3</span> Neural Networks (**Due 10/6 11:59pm**)  | [PDF](docs/hw3.pdf) / [Files](https://drive.google.com/file/d/1GWEzMWkNszGOG1oKJOVgWI87hMeNQCHY/view?usp=sharing) |

### Week 6

|  9/26 | <span class="label">Lecture 10</span> Neural Networks - CNNs, Batch Norm, & ResNets  | [Slides](docs/lec10.pdf) / [Recording](https://drive.google.com/file/d/1FORFqiwPvRe6gfbk2WQzCLMVBsGnUZLj/view?usp=drive_link) |
|  9/27 | <span class="label label-green">Discussion 4</span> Neural Networks and Training  | [PDF](docs/dis4.pdf) / [Solutions](docs/dis4_sol.pdf) / [Walkthrough](https://drive.google.com/file/d/16yz9ACJT4p373jNBOjGjvzT5fISARvij/view) |
|  9/28 | <span class="label">Lecture 11</span> Neural Networks - Attention & Transformers  | [Slides](docs/lec11.pdf) / [Recording](https://drive.google.com/file/d/1jhCDH6i9Ve-XSQNiF5vFpnlow0ieeB4V/view?usp=drive_link) |

### Week 7

|  10/3 | <span class="label">Lecture 12</span> Dimensionality Reduction & PCA  | [Slides](docs/lec12.pdf) / [Recording](https://drive.google.com/file/d/1p4-pCnWqqxabEEN_ViOwx5jpyiu1F26D/view?usp=drive_link) |
|  10/4 | <span class="label label-green">Discussion 5</span> Convolution and Attention  | [PDF](docs/dis5.pdf) / [Solutions](docs/dis5_sol.pdf) / [Walkthrough](https://drive.google.com/file/d/1xoZjEZRNOQp_R5Yf6Dg2VJhf_RPCIWkR/view) |
|  10/5 | <span class="label">Lecture 13</span> t-SNE  | [Slides](docs/lec13.pdf) / [Recording](https://drive.google.com/file/d/135K6w4zY8mNRLNN70xFr2IeYmhtPneqp/view?usp=drive_link) |
|  10/7 | <span class="label label-yellow">Homework 4</span> Dimensionality Reduction & Decision Theory (**Due 10/20 11:59pm**)  | [PDF](docs/hw4.pdf) / [Files](https://drive.google.com/file/d/1fuGXhyK8s3ewtdL-cvohxiliPDEVNbbk/view) |

### Week 8

|  10/10 | <span class="label">Lecture 14</span> Clustering  | [Slides](docs/lec14.pdf) / [Recording](https://drive.google.com/file/d/1Cb4OpSgClxXIGAp0vOpAxrm3U5DgH-tR/view?usp=drive_link) |
|  10/11 | <span class="label label-green">Discussion 6</span> Dimensionality Reduction Techniques  | [PDF](docs/dis6.pdf) / [Solutions](docs/dis6_sol.pdf) |
|  10/12 | <span class="label">Lecture 15</span> Multiway Classification, Decision Theory, & Model Evaluation  | [Slides](docs/lec15.pdf) / [Recording](https://drive.google.com/file/d/1YCW8JVfnng8B81jbslDCbPKI71UfjxUm/view?usp=share_link) |
|  10/13 | <span class="label label-red">Midterm</span> (7-9pm, Pimentel 1)  | [Blank](docs/mt.pdf) / [Solutions](docs/mt_sol.pdf) |

### Week 9

|  10/17 | <span class="label">Lecture 16</span> Nearest Neighbors & Metric Learning | [Slides](docs/lec16.pdf) / [Recording](https://drive.google.com/file/d/1KcAA23MObxrCogxUi8JYKmAU6zK3Obwa/view?usp=share_link) |
|  10/18 | <span class="label label-green">Discussion 7</span> Clustering and Decision Theory  | [PDF](docs/dis7.pdf) / [Solutions](docs/dis7_sol.pdf) / [Walkthrough](https://drive.google.com/file/d/1aKq1n6ddIUYroqh0rQloyCikweLBHFnL/view?usp=sharing) |
|  10/19 | <span class="label">Lecture 17</span> Decision Trees & Ensembling | [Slides](docs/lec17.pdf) / [Recording](https://drive.google.com/file/d/1vsh2ZVFbl4awo1GbubQKkM0fxrLoCx6Z/view?usp=share_link) |
|  10/21 | <span class="label label-yellow">Homework 5</span> Bias/Variance, Nearest Neighbors, Decision Trees (**Due 11/3 11:59pm**)  | [PDF](docs/hw5.pdf) / [Files](https://static.us.edusercontent.com/files/YjV6vY4SdO4oKCPvDW5xxyCI) |

### Week 10

|  10/24 | <span class="label">Lecture 18</span> Bias-Variance Tradeoff & Over/Under-Fitting | [Slides](docs/lec18.pdf) |
|  10/25 | <span class="label label-green">Discussion 8</span> Bias/Variance and Nearest Neighbors  | [PDF](docs/dis8.pdf) |
|  10/26 | <span class="label">Lecture 19</span> Hidden Markov Models & Graphical Models 1  |  |

### Week 11

|  10/31 | <span class="label">Lecture 20</span> Hidden Markov Models & Graphical Models 2  |  |
|  11/1 | <span class="label label-green">Discussion 9</span> Decision Trees and HMMs Intro  |  |
|  11/2 | <span class="label">Lecture 21</span> Markov Decision Processes  |  |
|  11/4 | <span class="label label-yellow">Homework 6</span> Markovian Models & Reinforcement Learning (**Due 11/17 11:59pm**)  |  |

### Week 12

|  11/7 | <span class="label">Lecture 22</span> Reinforcement Learning  |  |
|  11/8 | <span class="label label-green">Discussion 10</span> HMMs Advanced and MDPs  |  |
|  11/9 | <span class="label">Lecture 23</span> Robotics and Machine Learning  |  |

### Week 13

|  11/14 | <span class="label">Lecture 24</span> Language and Vision Applications  |  |
|  11/15 | <span class="label label-green">Discussion 11</span> Robotics, Language, & Vision  |  |
|  11/16 | <span class="label">Lecture 25</span> Graph Neural Networks & Rotational Equivariance 1  |  |
|  11/18 | <span class="label label-yellow">Homework 7</span> Graph Neural Networks & Applications of Deep Learning (**Due 12/1 11:59pm**)  |  |

### Week 14

|  11/21 | <span class="label">Lecture 26</span> Graph Neural Networks & Rotational Equivariance 2   |  |
|  11/22 | <span class="label label-green">Discussion 12</span> Graph Neural Networks  |  |
|  11/23 | No Lecture (Thanksgiving)  |  |

### Week 15

|  11/28 | <span class="label">Lecture 27</span> Special Topics - Computational Biology  |  |
|  11/30 | <span class="label label-green">Discussion 13</span> Special Topics - Causality  |  |

### Week 16 (RRR Week)

|  No lectures or discussions this week  |

### Week 17 (Finals Week)

|  12/12 | <span class="label label-red">Final Exam</span> (8-11am, Location TBD) |  |

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

**University of California, Berkeley**, Fall 2024

Welcome to CS 189/289A! This class covers theoretical foundations, algorithms, methodologies, and applications for machine learning. Topics may include supervised methods for regression and classication (linear models, trees, neural networks, ensemble methods, instance-based methods); generative and discriminative probabilistic models; deep learning models including CNNs, transformers, graph neural networks for vision and language tasks; and Markovian models for reinforcement learning and robotics.

**Textbook:** [_Deep Learning_](https://www.bishopbook.com/) by Bishop and Bishop.

Professors will post slides prior to lecture at this Google Drive [folder](https://drive.google.com/drive/folders/1hM6_gb8-cel4-hQ9_sMcm9krwfzmppkU?usp=drive_link) (for faster access). The material here is redundant with the website, but it may take up to a day or two for the website to get updated with the slides after lecture. The "Post-Lecture" subfolder contains updates to slides that the professors may make right after lecture. In addition, lecture recordings will be uploaded automatically to this Haas Panopto [folder](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID=%22380bd203-98f7-4a83-946e-b1d401302c37%22).

If you have not been added to **EdStem**, you may join through this [link](https://edstem.org/us/join/RUHntB).

**Note:** The topics for future lectures, discussions, and HWs are **tentative** and may be moved around, changed, or removed.

## Overview

### Week 1

|  8/29 | <span class="label">Lecture 1</span> [Introduction and Logistics](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2a2b47b1-dc5f-41e4-8258-b1d4013efe89) ([Slides](https://drive.google.com/file/d/1B-ikDeLJy045W0cw4qpP616MQXSRpqQh/view?usp=drive_link)) | <span class="label label-purple">Reading</span>  1.1-1.2.4 |
|  | <span class="label label-yellow">Homework 1</span> Math Review <nobr>(<strong>Due</strong> <s>9/11</s> <strong>9/12 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw1.pdf) / [Files](docs/hw_fa24/hw1.zip) / [LaTeX Template](docs/hw_fa24/hw1_template.tex) |


### Week 2

|  9/3 | <span class="label">Lecture 2</span> [Maximum Likelihood Estimation](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=78393f71-f7d8-4877-8ae4-b1d4013efedc) ([Slides](https://drive.google.com/file/d/1BsohO4nidHSdP3eZtWmcAN9mAMvID4B2/view?usp=sharing)) | <span class="label label-purple">Reading</span> <br> 2-2.1.2 (rules of probability: sum, product) <br> 2.1.6 (independent RVs) <br> 2.2-2.2.1 (probability densities in continuous spaces) <br> 2.3-2.3.2 (univariate Gaussian, likelihood) <br> 3-3.1.3 (Bernoulli, binomial, multinomial, MLE) |
|  | <span class="label label-green">Discussion 0</span> Math Pre-Requisites Review  | [Worksheet](docs/dis_fa24/dis0.pdf) / [Solutions](docs/dis_fa24/dis0sol.pdf)|
|  9/5 | <span class="label">Lecture 3</span> [Multivariate Gaussians](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eeb87936-eb47-436b-b6e5-b1d4013efefb) ([Slides](https://drive.google.com/file/d/11ozzwYUqyJnHeCxbKE9TL-kgZAyrykN5/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 3-3.2.3 (multivariate Gaussians: geometry, moments, covariance forms) |

### Week 3

|  9/10 | <span class="label">Lecture 4</span> Linear Regression 1  | <span class="label label-purple">Reading</span> <nobr>4-4.1.4</nobr> |
|  | <span class="label label-green">Discussion 1</span> MLE & Gaussians  |   |
|  9/12 | <span class="label">Lecture 5</span> Linear Regression 2  |  |
|  | <span class="label label-yellow">Homework 2</span> Linear/Logistic Regression & Classification <nobr>(<strong>Due 9/25 11:59pm</strong>)</nobr>  |  |

### Week 4

|  9/17 | <span class="label">Lecture 6</span> Classification - Generative & Discriminative  |  |
| | <span class="label label-green">Discussion 2</span> Linear Regression  |  |
|  9/19 | <span class="label">Lecture 7</span> Logistic Regression & Neural Networks  |  |

### Week 5

|  9/24 | <span class="label">Lecture 8</span> Backpropagation and Gradient Descent 1  |  |
|  | <span class="label label-green">Discussion 3</span> Classification & Logistic Regression  |  |
|  9/26 | <span class="label">Lecture 9</span> Backpropagation and Gradient Descent 2  |  |
|  | <span class="label label-yellow">Homework 3</span> Neural Networks <nobr>(<strong>Due 10/9 11:59pm</strong>)</nobr>  |  |

### Week 6

|  10/1 | <span class="label">Lecture 10</span> Neural Networks - CNNs, Batch Norm, & ResNets  |  |
|  | <span class="label label-green">Discussion 4</span> Neural Networks and Training  |  |
|  10/3 | <span class="label">Lecture 11</span> Neural Networks - Attention & Transformers  |  |

### Week 7

|  10/8 | <span class="label">Lecture 12</span> Dimensionality Reduction & PCA  |  |
|  | <span class="label label-green">Discussion 5</span> Convolution and Attention  |  |
|  10/10 | <span class="label">Lecture 13</span> t-SNE  |  |
|  | <span class="label label-yellow">Homework 4</span> Dimensionality Reduction & Decision Theory <nobr>(<strong>Due 10/23 11:59pm</strong>)</nobr>  |  |

### Week 8

|  10/15 | <span class="label">Lecture 14</span> Clustering  |  |
|  | <span class="label label-green">Discussion 6</span> Dimensionality Reduction Techniques  |  |
|  10/16 | <span class="label label-red">Midterm</span> (7-9pm, Location TBD)  |  |
|  10/17 | <span class="label">Lecture 15</span> Multiway Classification, Decision Theory, & Model Evaluation  |  |

### Week 9

|  10/22 | <span class="label">Lecture 16</span> Nearest Neighbors & Metric Learning |  |
|  | <span class="label label-green">Discussion 7</span> Clustering and Decision Theory  |  |
|  10/24 | <span class="label">Lecture 17</span> Decision Trees & Ensembling |  |
|  | <span class="label label-yellow">Homework 5</span> Bias/Variance, Nearest Neighbors, Decision Trees <nobr>(<strong>Due 11/6 11:59pm</strong>)</nobr>  |  |

### Week 10

|  10/29 | <span class="label">Lecture 18</span> Bias-Variance Tradeoff & Over/Under-Fitting |  |
|  | <span class="label label-green">Discussion 8</span> Bias/Variance and Nearest Neighbors  |  |
|  10/31 | <span class="label">Lecture 19</span> Hidden Markov Models & Graphical Models 1  |  |

### Week 11

|  11/5 | <span class="label">Lecture 20</span> Hidden Markov Models & Graphical Models 2  |  |
|  | <span class="label label-green">Discussion 9</span> Decision Trees and HMMs Intro  |  |
|  11/7 | <span class="label">Lecture 21</span> Markov Decision Processes  |  |
|  | <span class="label label-yellow">Homework 6</span> Markovian Models & Reinforcement Learning <nobr>(<strong>Due 11/20 11:59pm</strong>)</nobr>  |  |

### Week 12

|  11/12 | <span class="label">Lecture 22</span> Reinforcement Learning  |  |
|  | <span class="label label-green">Discussion 10</span> HMMs Advanced and MDPs  |  |
|  11/14 | <span class="label">Lecture 23</span> Robotics and Machine Learning  |  |

### Week 13

|  11/19 | <span class="label">Lecture 24</span> Graph Neural Networks & Rotational Equivariance 1  |  |
|  | <span class="label label-green">Discussion 11</span> MDPs & Reinforcement Learning |  |
|  11/21 | <span class="label">Lecture 25</span> Graph Neural Networks & Rotational Equivariance 2 |  |
|  | <span class="label label-yellow">Homework 7</span> Graph Neural Networks & Applications of Deep Learning <nobr>(<strong>Due 12/4 11:59pm</strong>)</nobr>  |  |

### Week 14

|  11/26 | <span class="label">Lecture 26</span> Language and Vision Applications |  |
|  11/28 | No Lecture (Thanksgiving)  |  |

### Week 15

|  12/3 | <span class="label">Lecture 27</span> Special Topics - Causality  |  |
|   | <span class="label label-green">Discussion 12</span> Graph Neural Networks  |  |
|  12/5 | <span class="label">Lecture 28</span> Special Topics - Computational Biology |  |

### Week 16 (RRR Week)

|  No lectures or discussions this week  |

### Week 17 (Finals Week)

|  12/17 | <span class="label label-red">Final Exam</span> (8-11am, location TBD) |  |

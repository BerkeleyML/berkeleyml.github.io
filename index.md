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

If you have not been added to **EdStem**, you may join through this [link](https://edstem.org/us/join/RUHntB). The **Gradescope** code is **DKPWZW**.

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

|  9/10 | <span class="label">Lecture 4</span> [Linear Regression 1](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0b684900-3ef3-411e-bb68-b1d4013eff13) ([Slides](https://drive.google.com/file/d/14vblwqegBN7BC8-l1sAsRmiEVIu0TFmR/view?usp=drive_link)) | <span class="label label-purple">Reading</span> <nobr>4-4.1.4</nobr> |
|  | <span class="label label-green">Discussion 1</span> MLE & Gaussians  | [Worksheet](docs/dis_fa24/dis1.pdf) / [Solutions](docs/dis_fa24/dis1sol.pdf) |
|  9/12 | <span class="label">Lecture 5</span> [Linear Regression 2](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=56e9bd90-5e0c-4333-bbac-b1d4013eff2e) ([Slides](https://drive.google.com/file/d/1S8WxurxGYTv6BZs3LGCHSR-tYkEvV8bC/view?usp=drive_link))  | <span class="label label-purple">Reading</span> <br> 1.25-1.26 (regularization, model selection) <br> 2.1.3 (Bayes theorem) <br> 2.6 (Bayesian modeling) <br> 4.1.6 (regularization for linear regression) <br> 9.2.2 (Lasso regularization) |
|  | <span class="label label-yellow">Homework 2</span> Linear/Logistic Regression & Classification <nobr>(<strong>Due 9/25 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw2.pdf) / [Files](docs/hw_fa24/hw2.zip) / [LaTeX Template](docs/hw_fa24/hw2template.tex) |

### Week 4

|  9/17 | <span class="label">Lecture 6</span> [Classification - Generative & Discriminative](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e0e7d595-678f-4064-a105-b1d4013eff4f) ([Slides](https://drive.google.com/file/d/1-g3MKFW9lDqYA9nRz9RbpPaztAFvVszq/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 5.1, 5.2.1, 5.2.2, 5.2.4, 5.3 |
| | <span class="label label-green">Discussion 2</span> Regularization & MAP  | [Worksheet](docs/dis_fa24/dis2.pdf) / [Solutions](docs/dis_fa24/dis2sol.pdf) |
|  9/19 | <span class="label">Lecture 7</span> [Logistic Regression & Neural Networks](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a245360c-f0f3-4b7d-bd8d-b1d4013eff6c) ([Slides](https://drive.google.com/file/d/1MSqZtGFwyzRe6RD-MNKDIrfYvORK1TvO/view?usp=drive_link))  | <span class="label label-purple">Reading</span> 5.3.1, 5.4.1-5.4.4, 6.1-6.2 |

### Week 5

|  9/24 | <span class="label">Lecture 8</span> [Backpropagation and Gradient Descent 1](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=27000014-6252-4b89-a499-b1d4013eff92) ([Slides](https://drive.google.com/file/d/1vfk8jqrsUay0J9IB-IPMnHwOp3IOZSnd/view?usp=drive_link))  | <span class="label label-purple">Reading</span> 6.2, 6.4, 7.1, 7.2, 5.4.4 |
|  | <span class="label label-green">Discussion 3</span> Classification & Logistic Regression  | [Worksheet](docs/dis_fa24/dis3.pdf) / [Solutions](docs/dis_fa24/dis3sol.pdf) |
|  9/26 | <span class="label">Lecture 9</span> [Backpropagation and Gradient Descent 2](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9ac17588-cef2-45f7-acd5-b1d4013effaf) ([Slides](https://drive.google.com/file/d/17tf2EgsyLHTAus6azWdTRSZH4cNkd2-4/view?usp=sharing))  | <span class="label label-purple">Reading</span> 5.4.4, 8 |
|  | <span class="label label-yellow">Homework 3</span> Neural Networks <nobr>(<strong>Due 10/9 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw3.pdf) / [Files](docs/hw_fa24/hw3.zip) / [LaTeX Template](docs/hw_fa24/hw3template.tex) |

### Week 6

|  10/1 | <span class="label">Lecture 10</span> [Neural Networks - CNNs, Batch Norm, & ResNets](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=90e02259-b095-494f-a363-b1d4013effc7) ([Slides](https://drive.google.com/file/d/1KVk_pfkzSkofNzwDo3kTLQosWOD9Y1gg/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 7.4, 9.5, 10 |
|  | <span class="label label-green">Discussion 4</span> Neural Networks and Backpropagation  | [Worksheet](docs/dis_fa24/dis4.pdf) / [Solutions](docs/dis_fa24/dis4sol.pdf) |
|  10/3 | <span class="label">Lecture 11</span> [Neural Networks - Attention & Transformers](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=42f09b54-f2f8-48ea-9e10-b1d4013effe9) ([Slides](https://drive.google.com/file/d/1IFyzNFeuLwuqOyC4ro90PMTuppCAGnND/view?usp=sharing))  | <span class="label label-purple">Reading</span> 5.3, 12.1 |

### Week 7

|  10/8 | <span class="label">Lecture 12</span> [Dimensionality Reduction & PCA](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5af23bc9-902e-4a00-8fda-b1d4013f0009) ([Slides](https://drive.google.com/file/d/1LJUJsVbpbwUWS9veFofSuzkOkIYjhNIw/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 16.1 |
|  | <span class="label label-green">Discussion 5</span> Convolution and Attention  | [Worksheet](docs/dis_fa24/dis5.pdf) / [Solutions](docs/dis_fa24/dis5sol.pdf) |
|  10/10 | <span class="label">Lecture 13</span> [t-SNE](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e60ff9dc-7403-4a84-b53d-b1d4013f0028) ([Slides](https://drive.google.com/file/d/1nWYPS98wNO2jVLvBMB32szsDOXu7edbQ/view?usp=drive_link)) |  |
|  | <span class="label label-yellow">Homework 4</span> Dimensionality Reduction & Decision Theory <nobr>(<strong>Due 10/25 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw4.pdf) / [Files](docs/hw_fa24/hw4.zip) / [LaTeX Template](docs/hw_fa24/hw4template.tex) |

### Week 8

|  10/15 | <span class="label">Lecture 14</span> [Clustering](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6b06ad21-49af-4254-9500-b1d4013f004c) ([Slides](https://drive.google.com/file/d/1I4sni1y5iXR7LjdBQ1TMn5ZtDl7Umrp3/view?usp=drive_link))  | <span class="label label-purple">Reading</span> 15.1 (not including 15.1.1), 15.2 |
|  | <span class="label label-green">Discussion 6</span> Dimensionality Reduction Techniques  | [Worksheet](docs/dis_fa24/dis6.pdf) / [Solutions](docs/dis_fa24/dis6sol.pdf) |
|  10/16 | <span class="label label-red">Midterm</span> (7-9pm, Dwinelle 155)  |  |
|  10/17 | <span class="label">Lecture 15</span> [Nearest Neighbors & Metric Learning](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e28b1ff9-717c-4217-b592-b1d4013f0085) ([Slides](https://drive.google.com/file/d/1p6uiI2y1ZCKCouFpxoJ72yC1JmPS2Df1/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 3.5, 6.3.5 |

### Week 9

|  10/22 | <span class="label">Lecture 16</span>  [Model Evaluation](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=194fc155-3acd-4009-a3c3-b1d4013f00a7) ([Slides](https://drive.google.com/file/d/16xXuolUV9K14jYSI4_xggsLgt6xPn9CY/view?usp=sharing)) | <span class="label label-purple">Reading</span> 5.25, 5.26 |
|  | <span class="label label-green">Discussion 7</span> Gaussian Mixture Models  | [Worksheet](docs/dis_fa24/dis7.pdf) / [Solutions](docs/dis_fa24/dis7sol.pdf) |
|  10/24 | <span class="label">Lecture 17</span> [Decision Trees & Ensembling](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5a92474e-2705-41f1-bfe7-b1d4013f00ce) ([Slides](https://drive.google.com/file/d/1U5EFGq1NkYKdy4xSMB-CI7FP-2_4pgxM/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 9.6 not including 9.6.1 (model averaging) |
|  | <span class="label label-yellow">Homework 5</span> Bias/Variance, Nearest Neighbors, Decision Trees <nobr>(<strong>Due 11/8 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw5.pdf) / [Files](docs/hw_fa24/hw5.zip) / [LaTeX Template](docs/hw_fa24/hw5template.tex) |

### Week 10

|  10/29 | <span class="label">Lecture 18</span> [Bias-Variance Tradeoff & Over/Under-Fitting](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a00177aa-d77e-4098-b867-b1d4013f00f1) ([Slides](https://drive.google.com/file/d/1bWeLeK3xaIQrUr-oUQVjOVGOnxQhg3Vo/view?usp=drive_link)) |  <span class="label label-purple">Reading</span> 4.2, 4.3, 9.3.2 |
|  | <span class="label label-green">Discussion 8</span> Bias/Variance, Decision Trees, & Nearest Neighbors  | [Worksheet](docs/dis_fa24/dis8.pdf) / [Solutions](docs/dis_fa24/dis8sol.pdf) |
|  10/31 | <span class="label">Lecture 19</span> [Hidden Markov Models & Graphical Models 1](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1cb78411-61e2-43d7-9c93-b1d4013f0112) ([Slides](https://drive.google.com/file/d/1lpj2Ax6fU1ei--5GJqw35YT-5gg45zjD/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 11 |

### Week 11

|  11/5 | <span class="label">Lecture 20</span> [Hidden Markov Models & Graphical Models 2](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=9ecbbdee-d01b-4f10-810c-b1d4013f0132) ([Slides](https://drive.google.com/file/d/1i9UX9FwgKjfpYgKlnFIJuPXjmj9gwxXw/view?usp=sharing))  |  <span class="label label-purple">Reading</span> Bishop 11; [Barber](http://web4.cs.ucl.ac.uk/staff/D.Barber/textbook/090310.pdf) 23.2.2, 23.2.5 |
|  | <span class="label label-green">Discussion 9</span> Random Forests and HMMs Intro  | [Worksheet](docs/dis_fa24/dis9.pdf) / [Solutions](docs/dis_fa24/dis9sol.pdf) |
|  11/7 | <span class="label">Lecture 21</span> [Generative Models 1](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=01b09f69-c06d-4faf-9dc7-b1d4013f0152) ([Slides](https://drive.google.com/file/d/1NL-JzwKWoF8OfODRVzt2mmFhcsaCKzIp/view?usp=sharing))  |  <span class="label label-purple">Reading</span> 14.3 |
|  | <span class="label label-yellow">Homework 6</span> Graphical Models & Langevin MCMC <nobr>(<strong>Due 11/20 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw6.pdf) / [Files](docs/hw_fa24/hw6.zip) / [LaTeX Template](docs/hw_fa24/hw6template.tex) |

### Week 12

|  11/12 | <span class="label">Lecture 22</span> [Generative Models 2](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6b1316da-dbfa-41ba-b546-b1d4013f0178) ([Slides](https://drive.google.com/file/d/1LY_43MV4uLmWF9IYHDt818k44mTkTWcU/view?usp=drive_link)) | <span class="label label-purple">Reading</span> 20.3 |
|  | <span class="label label-green">Discussion 10</span> Langevin Sampling | [Worksheet](docs/dis_fa24/dis10.pdf) / [Solutions](docs/dis_fa24/dis10sol.pdf) |
|  11/14 | <span class="label">Lecture 23</span> [Markov Decision Processes & Reinforcement Learning](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f35157a8-cfa3-468e-8076-b1d4013f019c) ([Slides](https://drive.google.com/file/d/1fiZbMjC1Z14l8Lx83v97rYibhytvClXz/view?usp=sharing))  |  |

### Week 13

|  11/19 | <span class="label">Lecture 24</span> [Graph Neural Networks & Rotational Equivariance 1](https://berkeley-haas.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7a341980-ce54-4ae4-aba6-b1d4013f01d7) ([Slides](https://drive.google.com/drive/folders/1FqQmhLf9UPIkN8qJKrY_QayFKN6OhZyL))  | <span class="label label-purple">Reading</span> 13 |
|  | <span class="label label-green">Discussion 11</span> Score Matching; MDPs & Reinforcement Learning | [Worksheet](docs/dis_fa24/dis11.pdf) |
|  11/21 | <span class="label">Lecture 25</span> Graph Neural Networks & Rotational Equivariance 2 |  |
|  | <span class="label label-yellow">Homework 7</span> Graph Neural Networks & Applications of Deep Learning <nobr>(<strong>Due 12/6 11:59pm</strong>)</nobr>  | [PDF](docs/hw_fa24/hw7.pdf) / [Files](docs/hw_fa24/hw7code.zip) |

### Week 14

|  11/26 | <span class="label">Lecture 26</span> Kernel Methods |  |
|  11/28 | No Lecture (Thanksgiving)  |  |

### Week 15

|  12/3 | <span class="label">Lecture 27</span> Special Topics - Causality  |  |
|   | <span class="label label-green">Discussion 12</span> Graph Neural Networks  |  |
|  12/5 | <span class="label">Lecture 28</span> Special Topics - Computational Biology |  |

### Week 16 (RRR Week)

|  No lectures or discussions this week  |

### Week 17 (Finals Week)

|  12/17 | <span class="label label-red">Final Exam</span> (8-11am, location TBD) |  |

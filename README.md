# Demonstration of reusing pretrained models in ONNX format

This repo contains small demonstrations of loading ONNX format pretrained models, and applying them to simple example input feature vectors to produce predictions.

Jump to:

* [CourseTime prediction with pretrained models](#coursetime)
* [MedianProbHit prediction with pretrained models](#medianprobhit)
* [Installation](#install)

## <a name="coursetime"> Quick Start: Predicting course time completion </a>

To get started, just run the included script: `load_model_and_try_prediction.py`

```console
$ conda activate reuse_onnx_models
$ python load_model_and_try_prediction.py
```
Make sure you've [installed the reuse_onnx_models conda environment](#install).

Should work out of the box. But if needed, edit the script to set `resource_dir = 'mastre_coursetime/'`

**Expected output**
```
-----------------------
Example Input X-Factors
-----------------------
   Total_Beep_Test_Shuttles  Best_Vertical_Jump  Weight  Waist_Circumference  ...  speed_cRT  stroop_effect  vs_score  CourseTime_pre
0                        28                14.5    58.4                  726  ...        286           -0.5  -23.9375             457
1                        51                18.0    63.7                  760  ...        302           33.0   19.8125             492
2                        71                23.5    86.0                  907  ...        336          131.5   56.1250             614
3                        93                27.5    99.3                  993  ...        402          274.5   98.9375             749
4                       106                31.5   115.1                 1135  ...       1486          357.5  134.4380             896

[5 rows x 30 columns]

-----------------------
Predictions
-----------------------
Predicted Y-Factor: CourseTime_post

[[577.64136]
 [577.2043 ]
 [600.9819 ]
 [635.1708 ]
 [673.74146]]

```

## <a name="medianprobhit"> Predicting median probability of hit in a target marksmanship exercise </a>

Run the script: `load_model_and_try_prediction.py`

but first edit the script to set `resource_dir = 'mastre_medianprobhit/'`


**Expected output**
```
-----------------------
Example Input X-Factors
-----------------------
   Total_Beep_Test_Shuttles  Best_Vertical_Jump  Weight  Waist_Circumference  ...  speed_cRT  stroop_effect  vs_score  MedianProbHit_pre
0                        28                14.5    58.4                  726  ...        286           -0.5  -23.9375           0.571429
1                        51                18.0    63.7                  760  ...        302           33.0   19.8125           0.750000
2                        71                23.5    86.0                  907  ...        336          131.5   56.1250           0.857143
3                        93                27.5    99.3                  993  ...        402          274.5   98.9375           1.000000
4                       106                31.5   115.1                 1135  ...       1486          357.5  134.4380           1.000000

[5 rows x 30 columns]

-----------------------
Predictions
-----------------------

Predicted Y-Factor: MedianProbHit_post

[[0.68360674]
 [0.7701102 ]
 [0.86725914]
 [0.91872495]
 [0.98987734]]
```

## Predicting outputs for a simple toy problem with 100 input dimensions but only 2 "truly" relevant

Run the script: `load_model_and_try_prediction.py`

but first edit the script to set `resource_dir = 'toy_lasso/'`

**Expected output**

```
-----------------------
Example Input X-Factors
-----------------------
    x_col00   x_col01   x_col02   x_col03   x_col04   x_col05  ...   x_col94   x_col95   x_col96   x_col97   x_col98   x_col99
0 -2.309350 -2.594270 -1.960590 -2.804670 -2.404190 -2.179930  ... -2.709060 -1.921570 -3.443060 -2.571400 -2.417060 -2.286400
1 -1.863430 -1.659740 -1.459190 -1.561170 -1.554500 -1.573330  ... -1.182370 -1.513540 -2.107450 -1.116230 -1.098290 -1.558790
2  0.048866  0.087643  0.040582  0.042807  0.311507 -0.349499  ... -0.083751 -0.009049 -0.342972  0.068807  0.084226 -0.150238
3  1.147740  1.549840  1.143580  1.249950  1.591580  1.521500  ...  1.058470  1.542670  1.054830  1.395580  1.040530  1.299810
4  1.842200  3.006670  2.460370  1.606760  2.650340  2.616590  ...  2.300020  1.928070  2.271650  1.958500  2.099210  2.084800

[5 rows x 100 columns]

-----------------------
Predictions
-----------------------
Predicted Y-Factor: y

[[ 5.118286]
 [ 6.492633]
 [10.136808]
 [12.686414]
 [14.829741]]
 ```

## <a name="install"> Installation </a>

Requires:

* Python 3.6+
* Anaconda 4.8 or higher
* ONNX 1.6 or higher

Update 2020-04-16: Successfully tested on Mac OS X, Linux, and Windows 10


1) Install `conda` for environment and package management.

Links for installation of "minimal" version of conda:

<https://docs.conda.io/en/latest/miniconda.html>

Make sure this will edit your PATH (should be automatic on OS X and Linux).



2) Using conda, create the project specific environment (includes ONNX and all other python packages needed)

Use conda to install given platform specific instructions:

* [reuse_onnx_models-win-64.yml](./reuse_onnx_models-win-64.yml)
* [reuse_onnx_models-linux-64.yml](./reuse_onnx_models-linux-64.yml)
* [reuse_onnx_models-osx-64.yml](./reuse_onnx_models-osx-64.yml)

#### For Linux:

Open any terminal, then do:

```
$ conda env create -f reuse_onnx_models-linux-64.yml
```


#### For Mac OS X:

Open any terminal, then do:

```
$ conda env create -f reuse_onnx_models-osx-64.yml
```

#### For Windows 10:

Open the **Anaconda Prompt** (Instructions: <https://docs.anaconda.com/anaconda/install/verify-install/#conda>)

Then do:

```
$ conda env create -f reuse_onnx_models-win-64.yml
```

where the required environment YAML file is included in this repo: [reuse_onnx_models.yml](./reuse_onnx_models.yml)


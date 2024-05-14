# incompleter

This repository contains the source and data for the paper "Feedback-Directed Partial Execution". This paper introduces a technique called incompleter, which applies a set of mocking and unmocking rules to execute an incomplete Python code snippet. The mocker component constitutes a set of mocking rules that are inductively applied to an incomplete snippet based on error feedback. The goal of the mocker component is to partially execute the code snippet with mock definitions of undefined variables and functions. Then the unmocker component receives the mocked snippet and applies a set of deductive rules and neural prediction to infer the actual type of the mocked variables.

## Evaluation

The evaluation of incompleter primarily contains two research questions RQ1 and RQ2. RQ1 evaluates the ability of the mocker to execute and cover code. RQ2 evaluates the ability of the unmocker to correctly infer the actual types of mocked variables. Artifacts related to the research questions accompanied with this repository.

A further case study evaluates the bug finding ability of incompleter. As part of the case study, we select the YouTube-DL application from the [BugsInPy](https://github.com/soarsmu/BugsInPy) dataset. We introduce incompleteness in the known buggy code of YouTube-DL and let incompleter mock-then-unmock the buggy incomplete code. Finally, we evaluate whether the bug would still surface when using a mocked-then-unmocked version of the incomplete buggy code. Please follow this [link](https://github.com/anonymous606060/incompleter-casestudy) for more details about the case study.

## Running incompleter

From the root directory of the project run the following commands.

1. Build a docker image as follows:
   ```
   user@host> docker build -t incompleter-docker .
   ```
2. Run the docker container and open a shell inside the container as follows:
   ```
   user@host> docker run -it incompleter-docker /bin/bash
   ```
3. Run incompleter inside the docker container as follows:
   ```
   root@container:/app/src> python3 -m main.main <input_dir> -c
   ```

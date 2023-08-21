# Mould Growth Modeling and Analysis

## Table of Contents
- [Data Source](#data-source)
- [Modeling RHcrit](#modeling-rhcrit)
- [Mould Growth Model](#mould-growth-model)
- [Parameter Tuning](#parameter-tuning)
- [RHcrit Variations](#rhcrit-variations)
- [Conclusion and Results](#conclusion-and-results)

---

## Data Source
University of Reading Atmospheric Observatory Database - time series data with temperature (denoted as `Td`) and relative humidity (denoted as `RH`)for the July 1st to Sep 1st 2022, collected at 5-minute intervals. 

## Modeling RHcrit
A critical relative humidity (RHcrit) model was constructed based on the given temperature. The model is defined as:
The `RHcrit` values were then added as a new column to our dataset.

## Mould Growth Model
Using a set of predefined parameters and the VTT model, we calculated the Mould Index (M) and its rate of change (dM/dt) over time. The parameters used for the calculations included:
- Transition constants `k11` and `k12` for the mould growth rate.
- Constants `A`, `B`, and `C` for the maximum mould growth rate calculation.
- `p_T`, `p_RH`, and `p_C` which are parameters used to compute the mould growth rate based on temperature and relative humidity.
- `W` and `SQ` which represent wood type and wood surface quality.
- `C_decline`, a coefficient for the decline phase of mould growth.

## Parameter Tuning
To refine the model further and ensure that the mould index lies between 0 and 6, we conducted parameter tuning. We experimented with different values of parameters such as `p_T`, `p_RH`, `p_C`, and `C_decline`.

Two sets of parameters were tested:
1. `p_T = 0.68`, `p_RH = 13.9`, `p_C = 66.02`
2. `p_T = 0.34`, `p_RH = 6.95`, `p_C = 33.01`
For each parameter set, we iterated through `C_decline` values ranging from 0.1 to 1.0 in increments of 0.1.

## RHcrit Variations
Additionally, we evaluated the model's performance for varying values of `RHcrit` when `T > 20` to determine its impact on mould growth. The values tested were 50, 60, 70, and 80.

## Conclusion and Results
Through this comprehensive analysis, we were able to model the mould growth index and its rate of change over time using given environmental data. The optimal parameter set was determined to be `p_T = 0.34`, `p_RH = 6.95`, and `p_C = 33.01` with a `C_decline` of `0.1` (or the specific value you found optimal). 
[VTT_5MIN.ipynb](./VTT_5MIN.ipynb)




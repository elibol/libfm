libFM
=====

Library for factorization machines

web: http://www.libfm.org/

forum: https://groups.google.com/forum/#!forum/libfm

Factorization machines (FM) are a generic approach that allows to mimic most factorization models by feature engineering. This way, factorization machines combine the generality of feature engineering with the superiority of factorization models in estimating interactions between categorical variables of large domain. libFM is a software implementation for factorization machines that features stochastic gradient descent (SGD) and alternating least squares (ALS) optimization as well as Bayesian inference using Markov Chain Monte Carlo (MCMC).

Compile
=======
libFM has been tested with the GNU compiler collection and GNU make. libFM and the tools can be compiled with
> make all

Usage
=====
Please see the [libFM 1.4.2 manual](http://www.libfm.org/libfm-1.42.manual.pdf) for details about how to use libFM. If you have questions, please visit the [forum](https://groups.google.com/forum/#!forum/libfm).


Benchmark MovieLens
=====

To generate train/test split for MovieLens 10 million:
```bash
scripts/triple_format_to_libfm.pl -in ml-10m/ratings.dat -target 2 -delete_column 3 -separator "::"
python scripts/traintestsplit.py ml-10m/ratings.dat.libfm
```

The output for the above is already included in this repo:
```bash
unzip ml-10m.zip
```

To run the benchmark:
```bash
bin/libFM -task r -train ml-10m/ratings.dat.libfm.train -test ml-10m/ratings.dat.libfm.test -dim '1,1,512' -method sgd -regular '0,0,0.04' -init_stdev 0.1 -learn_rate 0.003 -iter 128 -rlog libfm.log
```

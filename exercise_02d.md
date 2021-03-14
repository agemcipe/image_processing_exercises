## Exercise 02d 

We assume that it is true that two smaller dilations compute a bigger dilation. But what methods needs more computations?
Let's start with the simplest case in terms of structuring element a 3x3 square. For one pixel in the output we have to compute the max over (at most) 9 pixels. A max operation can be broken down max(1,2,3) = max(1, max(2, 3)).
* *without composition*. The output image has N x N Pixels and the Erosion is of size M . Therefore we have to do (N x N) x (M x M) - 1 elementary comparisons
* *with decomposition*. The output image has N x N Pixels and the number of Pixels in each comparison is M - 1. Therefore we have to do (N x N ) x (M - 1) + (N x N) x (M - 1) elementary comparisons. Since there is no M x M term, we have to do fewer computations as in the case without compositions.

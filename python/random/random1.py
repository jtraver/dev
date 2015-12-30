#!/usr/bin/python

# 
import random
import apihelper
# 
# # len1 = random.randint(0, max_byte_array)
# # byte = random.randint(0, 255)
# # nbins = random.randint(0, max_list)
# # dtype = random.randint(0, 2)
# # htype = random.randint(0, len(basic) - 1)
# # dtype = random.randint(0, len(hashable) - 1)
# # dtype = random.randint(0, 1)
# # val = random.random() * random.randint(1, 100000)
# # val = random.randint(1, 100000)
# # nbins = random.randint(0, max_list)
# # dtype = random.randint(0, len(types) - 1)
# # nbins = random.randint(0, max_dict)
# # dtype = random.randint(0, len(basic) - 1)
# # nbins = random.randint(0, max_string)
# # random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # ))
# # nbins = random.randint(0, max_unicode)
# # u = unichr(random.randint(0, max_unicode_char))
# # c = random.randint(0, 1)
# # u = u + unichr(random.randint(0, max_unicode_char))
# # u = u + unichr(random.randint(0xd800, 0xdbff))
# # u = u + unichr(random.randint(0xdc00, 0xdfff))
# # dtype = random.randint(0, 1)
# # val = random.random() * random.randint(1, 100000)
# # val = random.randint(1, 100000)
# # btype = random.randint(0, 32)
# # nbins = random.randint(0, tot_bins)
# # dtype = random.randint(0, 2)
# # htype = random.randint(0, len(basic) - 1)
# 

print "random = %s" % str(random)
# # random = <module 'random' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.pyc'>
print "random = %s" % str(dir(random))
# # random = ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_acos', '_ceil', '_cos', '_e', '_exp', '_hashlib', '_hexlify', '_inst', '_log', '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'division', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
apihelper.info(random)

# 
# Random    
#     Random number generator base class used by bound module functions. Used to instantiate instances of Random to get generators that don't share state. Especially useful for multi-threaded programs, creating a different instance of Random for each thread, and using the jumpahead() method to ensure that the generated sequences seen by each thread don't overlap. Class Random can also be subclassed if you want to use a different basic generator of your own devising: in that case, override the following methods: random(), seed(), getstate(), setstate() and jumpahead(). Optionally, implement a getrandbits() method so that randrange() can cover arbitrarily large ranges.
# 
# SystemRandom
#     Alternate random number generator using sources provided by the operating system (such as /dev/urandom on Unix or CryptGenRandom on Windows). Not available on all systems (see os.urandom() for details).
# 
# WichmannHill
#     None
# 
# _BuiltinMethodType
#     <attribute '__doc__' of 'builtin_function_or_method' objects>
# 
# _MethodType
#     instancemethod(function, instance, class) Create an instance method object.
# 
# _acos     
#     acos(x) Return the arc cosine (measured in radians) of x.
# 
# _ceil     
#     ceil(x) Return the ceiling of x as a float. This is the smallest integral value >= x.
# 
# _cos      
#     cos(x) Return the cosine of x (measured in radians).
# 
# _exp      
#     exp(x) Return e raised to the power of x.
# 
# _hexlify  
#     b2a_hex(data) -> s; Hexadecimal representation of binary data. This function is also available as "hexlify()".
# 
# _log      
#     log(x[, base]) Return the logarithm of x to the given base. If the base not specified, returns the natural logarithm (base e) of x.
# 
# _sin      
#     sin(x) Return the sine of x (measured in radians).
# 
# _sqrt     
#     sqrt(x) Return the square root of x.
# 
# _test     
#     None
# 
# _test_generator
#     None
# 
# _urandom  
#     urandom(n) -> str Return n random bytes suitable for cryptographic use.
# 
# _warn     
#     Issue a warning, or maybe ignore it or raise an exception.
# 
# betavariate
#     Beta distribution. Conditions on the parameters are alpha > 0 and beta > 0. Returned values range between 0 and 1.
# 
# choice    
#     Choose a random element from a non-empty sequence.
# 
# expovariate
#     Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero. (The parameter would be called "lambda", but that is a reserved word in Python.) Returned values range from 0 to positive infinity if lambd is positive, and from negative infinity to 0 if lambd is negative.
# 
# gammavariate
#     Gamma distribution. Not the gamma function! Conditions on the parameters are alpha > 0 and beta > 0. The probability distribution function is: x ** (alpha - 1) * math.exp(-x / beta) pdf(x) = -------------------------------------- math.gamma(alpha) * beta ** alpha
# 
# gauss     
#     Gaussian distribution. mu is the mean, and sigma is the standard deviation. This is slightly faster than the normalvariate() function. Not thread-safe without a lock around calls.
# 
# getrandbits
#     getrandbits(k) -> x. Generates a long int with k random bits.
# 
# getstate  
#     Return internal state; can be passed to setstate() later.
# 
# jumpahead 
#     Change the internal state to one that is likely far away from the current state. This method will not be in Py3.x, so it is better to simply reseed.
# 
# lognormvariate
#     Log normal distribution. If you take the natural logarithm of this distribution, you'll get a normal distribution with mean mu and standard deviation sigma. mu can have any value, and sigma must be greater than zero.
# 
# normalvariate
#     Normal distribution. mu is the mean, and sigma is the standard deviation.
# 
# paretovariate
#     Pareto distribution. alpha is the shape parameter.
# 
# randint   
#     Return random integer in range [a, b], including both end points.
# 
# random    
#     random() -> x in the interval [0, 1).
# 
# randrange 
#     Choose a random item from range(start, stop[, step]). This fixes the problem with randint() which includes the endpoint; in Python this is usually not what you want.
# 
# sample    
#     Chooses k unique random elements from a population sequence. Returns a new list containing elements from the population while leaving the original population unchanged. The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices). Members of the population need not be hashable or unique. If the population contains repeats, then each occurrence is a possible selection in the sample. To choose a sample in a range of integers, use xrange as an argument. This is especially fast and space efficient for sampling from a large population: sample(xrange(10000000), 60)
# 
# seed      
#     Initialize internal state from hashable object. None or no argument seeds from current time or from an operating system specific randomness source if available. If a is not None or an int or long, hash(a) is used instead.
# 
# setstate  
#     Restore internal state from object returned by getstate().
# 
# shuffle   
#     x, random=random.random -> shuffle list x in place; return None. Optional arg random is a 0-argument function returning a random float in [0.0, 1.0); by default, the standard random.random.
# 
# triangular
#     Triangular distribution. Continuous distribution bounded by given lower and upper limits, and having a given mode value in-between. http://en.wikipedia.org/wiki/Triangular_distribution
# 
# uniform   
#     Get a random number in the range [a, b) or [a, b] depending on rounding.
# 
# vonmisesvariate
#     Circular data distribution. mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, which must be greater than or equal to zero. If kappa is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2*pi.
# 
# weibullvariate
#     Weibull distribution. alpha is the scale parameter and beta is the shape parameter.

iterations = 100 *1000 * 1000

startTime = new Date()
x = {}
for (i = 0; i < iterations; i++) {
    x[i] = 0
}


console.log(new Date() - startTime)

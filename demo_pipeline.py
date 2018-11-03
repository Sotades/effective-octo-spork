import tubo
from capitalize import capitalize
from filter_wordwith_i import filter_wordwith_i

text = ['italy', 'germany', 'brazil', 'france', 'england',
    'argentina', 'peru', 'united states', 'australia',
    'sweden', 'china', 'poland', 'portugal']


output = tubo.pipeline(
    text,
    filter_wordwith_i,
    capitalize,
)

for op in output:
    print(op)
#Source: https://stackoverflow.com/questions/65731002/attributeerror-module-apache-beam-has-no-attribute-dofn
import apache_beam as beam

class Func1(beam.DoFn):

    def process(self, x, *args, **kwargs):
        for _ in range(x[1]):
            yield dict(zip(['name','value'],x))

with beam.Pipeline() as pipe:
    row = (
        pipe
        | beam.Create([
            ('apple', 1),
            ('banana', 2),
            ('orange', 3),

        ])
        | beam.ParDo(Func1())
        | beam.Map(print)
    )
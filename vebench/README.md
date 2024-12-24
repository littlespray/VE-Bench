## Easy Use
VE-Bench can be installed with a single ``pip`` command. Since the model employs normalization during training, its output does not represent absolute scores. We **recommend performing comparisons between video pairs**, as demonstrated below:
```
pip install vebench
```
When comparing videos:
```
from vebench import VEBenchModel

evaluator = VEBenchModel()

score1 = evaluator.evaluate('A black-haired boy is turning his head', 'assets/src.mp4', 'assets/dst.mp4')
score2 = evaluator.evaluate('A black-haired boy is turning his head', 'assets/src.mp4', 'assets/dst2.mp4')
print(score1, score2) # Score1: 1.3563, Score2: 0.66194
```
from vebench import VEBenchModel

evaluator = VEBenchModel()

score1 = evaluator.evaluate('A black-haired boy is turning his head', 'assets/src.mp4', 'assets/dst.mp4')
score2 = evaluator.evaluate('A black-haired boy is turning his head', 'assets/src.mp4', 'assets/dst2.mp4')
print(score1, score2)
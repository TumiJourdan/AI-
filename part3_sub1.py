import chess.engine
engine = chess.engine.SimpleEngine.popen_uci('./stockfish', setpgrp=True)









engine.quit()
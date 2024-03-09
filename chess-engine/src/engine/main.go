package engine


import (
	"os"
	"runtime/pprof"
	"chess-engine/src/engine/moves"
	"chess-engine/src/engine/board"
	"chess-engine/src/engine/search"
)


func CheckWin(stateObj *board.GameState) string {
	legalMoves := moves.GenerateAllMoves(stateObj, false)

	if len(legalMoves) > 0 {return "not_terminal"}
	
	kingPos := board.PieceLists.BlackKingPos
	if stateObj.WhiteToMove {kingPos = board.PieceLists.WhiteKingPos}

	//set bitboard at king's position
	var kingPosBB uint64
	kingPosBB |= 1 << kingPos

	inCheck := (kingPosBB & stateObj.NoKingMoveBitBoard) != 0

	if inCheck {
		if stateObj.WhiteToMove {
			return "black_win"
		} else {
			return "white_win"
		}
	} else {
		return "draw"
	}
}


func CalculateMove(stateObj *board.GameState, moveTime int) *moves.Move {
	//NOTE: UCI will handle updating board
	
	//start profiling (go tool pprof -http=:8080 profile.prof)
	file, err := os.Create("profile.prof")
	if err != nil {panic(err)}

	pprof.StartCPUProfile(file)
	defer pprof.StopCPUProfile()
	
	move := search.GetBestMove(stateObj, moveTime)
	
	return move
}
export class Board{
    board: number [][];
    list: number[];
    nColumns: number;
    nRows: number;

    constructor(pWidth:number, pHeigth:number){
        this.list = [];
        this.board = [];
        this.nColumns = pWidth;
        this.nRows = pHeigth;
        for(let i=0; i<pWidth; i++){
            this.list = [];
            for(let j=0; j<pHeigth; j++){
                this.list[j]=0;
            }
            this.board[i]=this.list;
        }
    }

    status(coordX:number, coordY:number) : number{
        return this.board[coordX][coordY];
    }

    changesStatus(coordX:number, coordY:number){
        this.board[coordX][coordY] = this.board[coordX][coordY] === 0 ? 1 : 0;
    }

    checkBoard(){
        let tmpBoard: number [][] = [];
        for(let i=0; i<this.nColumns; i++){
            tmpBoard[i]= [];
            let aux: number[] = [];
            for(let j=0; j<this.nRows; j++){
                aux.push(this.checkRules(i,j));
            }
            tmpBoard[i] = aux;
        }
        this.board = [...tmpBoard];
    }

    checkRules(coordX: number, coordY:number): number{
        const width = this.board.length;
        const heigth = this.board[0].length;
        const xMenos = coordX - 1 < 0 ? width - 1 : coordX - 1;
        const xMas = coordX + 1 >= width ? 0 : coordX + 1;
        const yMenos = coordY - 1 < 0 ? heigth - 1 : coordY - 1;
        const yMas = coordY + 1 >= heigth ? 0 : coordY + 1;
        const currentStatus = this.board[coordX][coordY];
        const vecinos =
            this.board[xMenos][yMenos] +
            this.board[xMenos][coordY] +
            this.board[xMenos][yMas] +
            this.board[coordX][yMenos] +
            this.board[coordX][yMas] +
            this.board[xMas][coordY] +
            this.board[xMas][yMas] +
            this.board[xMas][yMenos];

        if(currentStatus === 1 && (vecinos === 2 || vecinos === 3)){
            return 1;
        }

        if(currentStatus === 0 && vecinos === 3){
            return 1;
        }

        return 0;
    }
}
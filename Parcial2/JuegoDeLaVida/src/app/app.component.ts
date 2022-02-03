import { Component } from '@angular/core';
import { Board } from './board.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'JuegoDeLaVida';
  numCols : number;
  numRows : number;
  generation : number;
  gameStatus : number;
  i : number = 0;
  board : Board;
  listaC:any[];
  listaR:any[];
  constructor(){
    this.numCols = 40;
    this.numRows = 40;
    this. generation = 0;
    this.gameStatus = 1;
    this.listaC=[];
    this.listaR=[];
    for(let i=0; i<this.numCols; i++){
      this.listaC[i]=i;
    }
    for(let i=0; i<this.numRows; i++){
      this.listaR[i]=i;
    }
    this.board = new Board(this.numCols, this.numRows);
  }

  ngOnInit(){
    setInterval(()=>{
      if ( this.gameStatus===0){
        this.board.checkBoard();
        this.generation++;
      }
    }, 100)
  }

  onClick(pRow:any, pCol:any){
    this.board.changesStatus(pRow,pCol);
  }

  onClickPausar(){
    this.gameStatus = this.gameStatus===0?1:0;
  }

  onClickIniciar(){
    if(this.gameStatus===1){
      this.gameStatus=0;
    }
  }
}

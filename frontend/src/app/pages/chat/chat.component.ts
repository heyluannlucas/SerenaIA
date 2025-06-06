import { Component, ElementRef, ViewChild } from '@angular/core';
import { ChatService } from '../../services/chat.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Mensagem {
  autor: 'usuario' | 'serena';
  texto: string;
}

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent {
  mensagens: Mensagem[] = [];
  entradaUsuario: string = '';
  carregando = false;

  @ViewChild('chatScroll') chatScroll!: ElementRef<HTMLDivElement>;

  constructor(private chatService: ChatService) {}

  enviar() {
    const mensagem = this.entradaUsuario.trim();
    if (!mensagem) return;

    this.mensagens.push({ autor: 'usuario', texto: mensagem });
    this.entradaUsuario = '';
    this.carregando = true;
    this.scrollToBottom();

    this.chatService.enviarMensagem(mensagem).subscribe({
      next: (res) => {
        this.mensagens.push({ autor: 'serena', texto: res.resposta });
        this.carregando = false;
        this.scrollToBottom();
      },
      error: () => {
        this.mensagens.push({
          autor: 'serena',
          texto: 'Desculpe, houve um erro ao se comunicar com a SerenaIA.'
        });
        this.carregando = false;
        this.scrollToBottom();
      }
    });
  }

  formatarTexto(texto: string): string {
    return texto
      .replace(/\n/g, '<br>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>');
  }

  scrollToBottom() {
    setTimeout(() => {
      if (this.chatScroll) {
        this.chatScroll.nativeElement.scrollTo({
          top: this.chatScroll.nativeElement.scrollHeight,
          behavior: 'smooth'
        });
      }
    }, 100);
  }
}

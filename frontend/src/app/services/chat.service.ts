import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ChatService {
  private apiUrl = 'http://localhost:5000/chat'; 

  constructor(private http: HttpClient) {}

  enviarMensagem(mensagem: string): Observable<{ resposta: string }> {
    return this.http.post<{ resposta: string }>(this.apiUrl, { mensagem });
  }
}

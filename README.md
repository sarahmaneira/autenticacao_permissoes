# autenticacao_permissoes

Requisitos:​

- O usuário deve entrar com o seu login e senha​ (autenticação) e ter a funcionalidade de cadastrar usuário
 * Se o usuário estiver autenticado, continue a execução do programa
 * Caso contrário, saia do programa e mostre a mensagem "Usuário ou senha inválidos" na tela
 * Um novo usuário cadastrado não deverá ter permissão para nenhum arquivo
- A relação usuário/senha deve estar armazenado em um arquivo (TXT, CSV ou JSON)
- As permissões dos usuários devem estar armazenadas em um arquivo (TXT, CSV ou JSON)
- O sistema deve perguntar ao usuário qual ação ele deseja realizar (ler, escrever ou apagar) sobre um recurso fictício
 * No contexto do trabalho, o recurso fictício, no caso, não é um arquivo existente no sistema
- Ele deverá especificar a ação que deseja realizar (ler, escrever, apagar) sobre um recurso
- O sistema deve perguntar ao usuário qual arquivo ele deseja realizar a operação selecionada no item 2​
- O sistema deve imprimir na tela caso o acesso foi concedido ou não​
 * “Acesso permitido” caso o acesso foi concedido​
 * Se não, “Acesso negado”
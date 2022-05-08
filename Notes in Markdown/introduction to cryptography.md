# Introdução à Criptografia

## Sumário
- [Conteúdo da disciplina]()
- [Contexto da criptografia]()
- [Problema Alice e Bob]()
- [Problemas de segurança na transmissão de dados em rede]()

## Conteúdo da disciplina 
A disciplina e lecionada em três pilares básicos:

- **Cifragem simétrica:** técnicas clássicas, cifragem de bloco e DES, teoria dos números e AES, cifragem múltipla, modos de operação, geração de números aleatórios, cifragem de fluxo e RC4;
- **Cifragem assimétrica:** primalidade, teoremas de Fermat, Euler e chinês do resto, logaritmo discreto, algoritmos baseados na fatoração de inteiros (RSA), algoritmos baseados no logaritmo discreto (Diffie-Hellman e Elgamal), criptografia por curvas elípticas;
- **Protocolos de segurança:** funções de hash criptográficas, códigos de autenticação de mensagens, assinatura digital, gerenciamento e distribuição de chave, autenticação de usuário.

## Contexto da criptografia
<p align="justify">A criptografia é a arte ou ciência de encriptar ou cifrar, em suma maioria com o objetivo de impedir terceiros de terem acesso a informação transmitida. Esta área pode abranger desde a segurança computacional e otimização de software até projetos de CIs (circuitos integrados), ciência forense, economia, física quântica, política e muito mais.

Algumas observações que devemos levar em conta é que a criptografia apenas será efetiva se o resto do sistema for suficientemente seguro, "*A chain is only as strong as its weakest link*".

- Não há segurança perfeita: A ideia por trás dos algoritmos de criptografia e manter-se open-sorce onde a segurança não deve estar presente no algoritmo e sim no método de geração das chaves e sua distribuição como e visto no príncipio de Kerckhoff;
- Criptografia não é solução pode ser parte da solução ou do problema;
- Segurança *vs* Desempenho: A complexidade e pressa são os maiores inimigos da segurança;
- Segurança *vs* Caraterísticas: Quanto mais opções de configuração, mais possibilidades de brechas.

## Problema Alice e Bob

<p align="justify">Aqui iremos introduzir um problema bem conhecido no mundo da segurança de redes chamado "Alice e Bob" onde Bob deseja se comunicar com Alice de uma forma segura e o nosso vilão chamado Darth deseja interceptar a mensagem e inferir o conteúdo da mesma, causando quatro questionamentos.

- **Confidencialidade:** apenas o remetente e o destinatário pretendido deveriam "entender" o conteúdo da mensagem.
- **Autenticação:** remetente e destinatário querem confirmar a identidade um do outro.
- **Integridade da mensagem:** remetente e destinatário querem assegurar que as mensagens não foram alteradas, (em trânsito, ou depois) sem detecção.
- **Acesso e disponibilidade:** serviços devem ser acessíveis e disponíveis para os usuários.
<br></br>
<center>Exemplo da comunicação entre Bob e Alice sendo interceptada por Darth</center>
<center>
<br/><img src="https://i.postimg.cc/tCnd4ZK9/Alice-Bob.png" ><br/>   
</center>
<br>

<p align="justify">Em comunicações como esta podemos se utilizar da criptografia simétrica onde os dois usuários se utilizam da mesma chave para encriptar e decriptar a mensagem, assim Alice e Bob podem se utilizar de uma chave denominada *K*, portanto Alice envia *Y = E(K,X)* e Bob recebe *X = D(K,Y)* como demonstrado no diagrama abaixo.

<center>
<br/><img src="https://i.postimg.cc/1zLQT0CV/Capturar.png" ><br/> 
</center>
<br>

<p align="justify">Se a encriptação for boa, Darth não obterá informações sobre X, exeto o comprimento e instante de transmissão. Para termmos certeza que Darth não interferiu em *X* devolvendo *X'* para Alice, Bob poderá criar um código de autenticação *A = h(K,X)* e transmite *(X,A)* assim Alice recebe *(X,A)*, gera localmente *h(K,X)* e compara com *A*. A função *h* mencionada pode ser considerada um algoritmo de hash que tem como função garantir que o arquivo não foi manipulado por terceiros durante a transmissão da mensagem, tendo uma identificação única, entraremos mais a fundo sobre esses algoritmos nas próximas aulas. Porém a autenticação não resolve tudo Darth poderá bloquear mensagens, retransmitir mensagens antigas ou mudar ordem de mensagens.

## Problemas de segurança na transmissão de dados em rede

<p align="justify">Se trouxermos Bob e Alice para o mundo real teriamos a relação entre Browser/Servidor Web (Cliente/Servidor) para transações eletrônicas por exemplo. Um dos problemas mais comuns são:

- Personificação: faslsificar (spoof) endereço de origem no pacote (ou qualquer campo no pacote)
- Hijacking: assume a conexão removendo o transmissor ou receptor e se inserindo no lugar
- Negação de serviço: conhecido como DDoS (distributed denial of service) impede que um determinado serviço seja utilizado por outros usuários devido a sobrecarga de recursos, em sua grande maioria as redes de BotNets que sobrecarregam um determinado serviço são compostas por dispositivos IoT, existem algumas soluções que podem mitigar esse tipo de ataque como espelhar diversos servidores que fornecem o mesmo serviço 
import streamlit as st
import random

def main():
    st.set_page_config(page_title="GERADOR DA MEGA SENA", layout="centered")
    
    # Menu de navegação
    menu = ["Boas-vindas", "Gerar Números", "Conferir Resultados"]
    escolha = st.sidebar.selectbox("Navegação", menu)
    
    if escolha == "Boas-vindas":
        pagina_boas_vindas()
    elif escolha == "Gerar Números":
        pagina_gerar_numeros()
    elif escolha == "Conferir Resultados":
        pagina_conferir_resultados()

def pagina_boas_vindas():
    st.title("Bem-vindo ao Gerador da Mega Sena!")
    st.markdown(
        """
        Este aplicativo possui duas funções principais:
        
        1. **Gerador de Números:** Gere 6 números aleatórios entre 1 e 60 para usar no seu jogo da Mega Sena.
        2. **Conferir Resultados:** Compare seus jogos com o resultado oficial para verificar quantos números você acertou.
        
        Use o menu lateral para navegar entre as páginas!
        """
    )

def pagina_gerar_numeros():
    st.title("Gerador de Números da Mega Sena")
    
    if st.button("Gerar Números"):
        numeros = sorted(random.sample(range(1, 61), 6))
        st.success(f"Seus números da sorte são: {', '.join(map(str, numeros))}")
    else:
        st.info("Clique no botão acima para gerar seus números da sorte.")

def pagina_conferir_resultados():
    st.title("🔢 Conferir Resultados da Mega Sena")
    
    # Entrada: Resultado oficial
    resultado_input = st.text_input(
        "Digite os 6 números sorteados (separados por vírgula):",
        placeholder="Exemplo: 05, 12, 23, 34, 45, 56"
    )
    
    # Entrada: Jogos do usuário
    jogos_input = st.text_area(
        "Digite seus jogos (um por linha, 6 números separados por vírgula):",
        placeholder="Exemplo:\n05, 12, 23, 34, 45, 56\n01, 02, 03, 04, 05, 06"
    )
    
    if st.button("Verificar"):
        try:
            # Processar os números do resultado
            resultado = [int(num.strip()) for num in resultado_input.split(",")]
            if len(resultado) != 6:
                st.error("Por favor, insira exatamente 6 números no resultado oficial.")
            else:
                # Processar os jogos do usuário
                jogos = [
                    [int(num.strip()) for num in jogo.split(",")]
                    for jogo in jogos_input.splitlines()
                    if jogo.strip()
                ]
                
                # Verificar acertos
                acertos = [len(set(jogo) & set(resultado)) for jogo in jogos]

                # Separar os jogos premiados
                jogos_premiados = [
                    (i, jogo, acerto)
                    for i, (jogo, acerto) in enumerate(zip(jogos, acertos), start=1)
                    if acerto == 6
                ]
                jogos_nao_premiados = [
                    (i, jogo, acerto)
                    for i, (jogo, acerto) in enumerate(zip(jogos, acertos), start=1)
                    if acerto != 6
                ]

                # Exibir resultados
                st.success("Conferência concluída!")
                if jogos_premiados:
                    st.markdown("### 🎉 Jogos Premiados:")
                    for i, jogo, acerto in jogos_premiados:
                        st.write(f"🎉 **Jogo {i}: {jogo} - Você acertou todos os 6 números! Está MILIONÁRIO!**")
                
                if jogos_nao_premiados:
                    st.markdown("### Jogos Não Premiados:")
                    for i, jogo, acerto in jogos_nao_premiados:
                        st.write(f"Jogo {i}: {jogo} - **{acerto} acertos**")
                
                if not jogos_premiados:
                    st.info("Nenhum jogo acertou todos os 6 números. Tente novamente na próxima vez!")
        except ValueError:
            st.error("Por favor, insira apenas números separados por vírgulas.")

if __name__ == "__main__":
    main()

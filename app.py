import streamlit as st

st.set_page_config(page_title="Calculadoras de IDE", layout="centered")

st.title("Calculadoras de IDE - Fundamental")

tab1, tab2, tab3 = st.tabs(["IDE Alfa", "IDE Anos Iniciais", "IDE Anos Finais"])

# Função de cálculo
def calcular_ide(tipo, **kwargs):
    if tipo == 1:
        LP1, LP2 = 0, 326
        notaLP = kwargs["notaLP"]
        aprovados = [kwargs["ap1"], kwargs["ap2"]]
        IR = 2 / sum(1 / a for a in aprovados)
        notaPadronizadaLP = ((notaLP - LP1) / (LP2 - LP1)) * 10
        notaPadronizadaMT = 0
        NP = notaPadronizadaLP

    elif tipo == 2:
        LP1, LP2 = 49, 324
        MT1, MT2 = 60, 322
        notaLP = kwargs["notaLP"]
        notaMT = kwargs["notaMT"]
        aprovados = [kwargs["ap3"], kwargs["ap4"], kwargs["ap5"]]
        IR = 3 / sum(1 / a for a in aprovados)
        notaPadronizadaLP = ((notaLP - LP1) / (LP2 - LP1)) * 10
        notaPadronizadaMT = ((notaMT - MT1) / (MT2 - MT1)) * 10
        NP = (notaPadronizadaLP + notaPadronizadaMT) / 2

    elif tipo == 3:
        LP1, LP2 = 100, 400
        MT1, MT2 = 100, 400
        notaLP = kwargs["notaLP"]
        notaMT = kwargs["notaMT"]
        aprovados = [kwargs["ap6"], kwargs["ap7"], kwargs["ap8"], kwargs["ap9"]]
        IR = 4 / sum(1 / a for a in aprovados)
        notaPadronizadaLP = ((notaLP - LP1) / (LP2 - LP1)) * 10
        notaPadronizadaMT = ((notaMT - MT1) / (MT2 - MT1)) * 10
        NP = (notaPadronizadaLP + notaPadronizadaMT) / 2

    IDE = NP * IR
    return notaPadronizadaLP, notaPadronizadaMT, NP, IR, IDE


with tab1:
    st.header("Cálculo do IDE Alfa")
    notaLP = st.number_input("Proficiência Média de Língua Portuguesa (2º Ano)", min_value=0.0)
    ap1 = st.number_input("Percentual de Aprovados do 1º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap2 = st.number_input("Percentual de Aprovados do 2º Ano (%)", min_value=0.0, max_value=100.0) / 100
    if st.button("Calcular IDE Alfa"):
        lp, mt, np, ir, ide = calcular_ide(1, notaLP=notaLP, ap1=ap1, ap2=ap2)
        st.write(f"**Nota Padronizada LP:** {lp:.2f}")
        st.write(f"**Nota Padronizada MT:** {mt:.2f}")
        st.write(f"**Média das Notas Padronizadas (NP):** {np:.2f}")
        st.write(f"**Indicador de Rendimento (IR):** {ir:.2f}")
        st.success(f"**IDE Escola:** {ide:.2f}")


with tab2:
    st.header("Cálculo do IDE Anos Iniciais")
    notaLP = st.number_input("Proficiência Média de Língua Portuguesa (5º Ano)", min_value=0.0)
    notaMT = st.number_input("Proficiência Média de Matemática (5º Ano)", min_value=0.0)
    ap3 = st.number_input("Percentual de Aprovados do 3º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap4 = st.number_input("Percentual de Aprovados do 4º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap5 = st.number_input("Percentual de Aprovados do 5º Ano (%)", min_value=0.0, max_value=100.0) / 100
    if st.button("Calcular IDE Anos Iniciais"):
        lp, mt, np, ir, ide = calcular_ide(2, notaLP=notaLP, notaMT=notaMT, ap3=ap3, ap4=ap4, ap5=ap5)
        st.write(f"**Nota Padronizada LP:** {lp:.2f}")
        st.write(f"**Nota Padronizada MT:** {mt:.2f}")
        st.write(f"**Média das Notas Padronizadas (NP):** {np:.2f}")
        st.write(f"**Indicador de Rendimento (IR):** {ir:.2f}")
        st.success(f"**IDE Escola:** {ide:.2f}")


with tab3:
    st.header("Cálculo do IDE Anos Finais")
    notaLP = st.number_input("Proficiência Média de Língua Portuguesa (9º Ano)", min_value=0.0)
    notaMT = st.number_input("Proficiência Média de Matemática (9º Ano)", min_value=0.0)
    ap6 = st.number_input("Percentual de Aprovados do 6º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap7 = st.number_input("Percentual de Aprovados do 7º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap8 = st.number_input("Percentual de Aprovados do 8º Ano (%)", min_value=0.0, max_value=100.0) / 100
    ap9 = st.number_input("Percentual de Aprovados do 9º Ano (%)", min_value=0.0, max_value=100.0) / 100
    if st.button("Calcular IDE Anos Finais"):
        lp, mt, np, ir, ide = calcular_ide(3, notaLP=notaLP, notaMT=notaMT, ap6=ap6, ap7=ap7, ap8=ap8, ap9=ap9)
        st.write(f"**Nota Padronizada LP:** {lp:.2f}")
        st.write(f"**Nota Padronizada MT:** {mt:.2f}")
        st.write(f"**Média das Notas Padronizadas (NP):** {np:.2f}")
        st.write(f"**Indicador de Rendimento (IR):** {ir:.2f}")
        st.success(f"**IDE Escola:** {ide:.2f}")


# New Load PS2 — protótipo de desenvolvimento 0.1

Base: PS2 Launcher 1.2.0. **Não é uma versão compilada nem testada no console.**

## Alterações efetivas
- Identificação na tela Sobre: New Load PS2.
- Rodapé da tela de ajustes visuais: NEW LOAD PS2 (sem ícone de rede social).
- Transição de seleção horizontal um pouco mais responsiva (fator 0.36 para 0.45).

## Já existente na base (não foi implementado por este patch)
- Interface com cartões quadrados e navegação horizontal.
- Modo visual especial (`gPS5Mode`) e recursos herdados do OPL.
- Fundo escuro (RGB 16,16,16 em `src/gui.c`).

## Pendente
- Auditoria de menus e recursos, localização PT-BR/EN, seleção de fundos e otimização mensurada.
- Compilação com PS2SDK/gsKit e dependências indicadas pelo Makefile.
- Testes em console real e validação de compatibilidade.

## Segurança
Não substitua seu OPL existente. Não há ELF neste pacote.

## Créditos
Fork experimental não oficial. Preservados README e LICENSE originais e seus créditos. Verifique as condições de redistribuição antes de publicar.

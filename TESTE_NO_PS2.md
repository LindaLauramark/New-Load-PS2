# New Load PS2 — preparação de teste

ESTE PACOTE É CÓDIGO-FONTE, NÃO É UM ELF PRONTO.

## Alteração nova
- Identificação discreta NEW LOAD PS2 no cabeçalho da interface horizontal existente, usando fonte já carregada (sem textura extra).
- Código de inicialização dos jogos mantido.

## Compilação
Requer PS2DEV, PS2SDK, gsKit, compiladores EE/IOP e dependências do Makefile, instalados e configurados em Linux ou WSL2. Execute `make -j2` na raiz do projeto e verifique o ELF gerado. O build NÃO foi validado neste ambiente.

## Teste seguro quando existir ELF
1. Mantenha uma cópia de segurança do Memory Card e seu OPL atual.
2. Copie o novo ELF para um pendrive FAT32, sem substituir arquivos existentes.
3. Abra-o por um gerenciador ELF já funcional (por exemplo, wLaunchELF).
4. Confira menus, lista de jogos, USB/HDD, controles e carregamento de um jogo que você possui.
5. Se ocorrer erro, reinicie e volte ao OPL original.

## Limitações
Não foi compilado nem testado em hardware. O suporte a temas, idiomas e todos os recursos do OPL ainda precisa de validação.

# python-ecommerce

## Instruções

1. Instale as dependências

```bash
pip3 install -r requirements.txt
```

2. Inicie o banco de dados

```bash
flask shell
> db.create_all()
> db.session.commit()
> exit()
```

3. Rode a aplicação

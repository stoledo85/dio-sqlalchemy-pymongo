"""Projeto do SQLAlchemy"""

from sqlalchemy.orm import declarative_base, relationship, Session

from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine,inspect

Base = declarative_base()
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)


class Cliente(Base):
    """Tabela Cliente"""

    __tablename__ = "tb_cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(11))
    endereco = Column(String(50))

    conta = relationship("Conta", back_populates="cliente")

    def __repr__(self) -> str:
        return f"Cliente(id={self.id!r}, nome={self.nome!r}, cpf={self.cpf!r},endereco={self.endereco!r})"


class Conta(Base):
    """Tablela Cliente"""

    __tablename__ = "tb_conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("tb_cliente.id"), nullable=False)
    saldo = Column(Float)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self) -> str:
        return f"Conta(id={self.id!r},tipo={self.agencia!r},num={self.num!r},saldo={self.saldo!r})"


insp = inspect(engine)
Base.metadata.create_all(engine)

#print(insp.get_table_names())

with Session(engine) as session:

    cliente1 = Cliente(
        nome="Eduarda Silva",
        cpf="25283378098",
        endereco="61296 Moreira Travessa",
        conta=[Conta(tipo="Conta Corrente", agencia="001", num="32728506", saldo=300.0)]
    )
    cliente2 = Cliente(
        nome="Washington Carvalho",
        cpf="87314185034",
        endereco="1819 Saraiva Alameda",
        conta=[Conta(tipo="Poupanca", agencia="001", num="82013781", saldo=950.0)]
    )

    session.add_all([cliente1, cliente2])
    session.commit()

print(Cliente.__tablename__)
print(Conta.__tablename__)

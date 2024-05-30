"""Projeto do SQLAlchemy"""

from sqlalchemy.orm import declarative_base, relationship, Session

from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine

Base = declarative_base()
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)


class Cliente(Base):
    """Tablela Cliente"""

    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )


class Conta(Base):
    """Tablela Cliente"""

    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    saldo = Column(Float)

    cliente = relationship("Cliente", back_populates="conta")


with Session(engine) as session:

    cliente1 = Cliente(
        nome="Eduarda Silva", cpf="25283378098", endereco="61296 Moreira Travessa"
    )
    cliente2 = Cliente(
        nome="Washington Carvalho", cpf="87314185034", endereco="1819 Saraiva Alameda"
    )

    # conta1 = Conta(
    #     tipo="Conta Corrente",
    #     agencia="001",
    #     num="32728506",
    #     id_cliente=Cliente(id="1"),
    #     saldo=300.00
    # )

    # conta2 = Conta(
    #     tipo="Poupanca",
    #     agencia="001",
    #     num="82013781",
    #     id_cliente=Cliente(id="2"),
    #     saldo=950.00
    # )

    # session.add_all([cliente1, cliente2, conta1, conta2])
    session.add_all([cliente1,cliente2])
    session.commit()

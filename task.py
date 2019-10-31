#!/usr/bin/env python3
from os import environ
import sys
import requests as req

serv_addr = "http://127.0.0.1:5000/" #environ["serv_addr"]

if sys.argv[1] == "add":     # adicionar [lista de valores dos atributos da classe]
    res = req.post(serv_addr + "todo/api/tasks/")
    print(res)

if sys.argv[1] == "list":    # listar
    res = req.get(serv_addr +" todo/api/tasks/")
    print(res)

if sys.argv[1] == "search":  # buscar
    res = req.get(serv_addr + "todo/api/tasks/" + sys.argv[2])
    print(res)

if sys.argv[1] == "delete":  # apagar
    res = req.delete(serv_addr + "todo/api/tasks/" + sys.argv[2])
    print(res) 

if sys.argv[1] == "update":  # atualizar [lista de valores dos atributos da classe]
    res = req.put(serv_addr + "todo/api/tasks/" + sys.argv[2])
    print(res)
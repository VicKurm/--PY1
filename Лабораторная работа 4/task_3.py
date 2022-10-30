def delete(list_, index=None):
    if index is not None:
        y = list_[:index]
        z = list_[index+1:]
        end_ = y + z
        return end_
    else:
        end_ = list_[:-1]
        return end_
    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

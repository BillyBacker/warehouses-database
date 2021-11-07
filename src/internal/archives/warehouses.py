from __future__ import annotations
from typing import Optional, Type, TypedDict

class TreeNode:
    def __init__(self, data: str, children: Optional[dict[str, Type[TreeNode]]]):
        self.data = data
        self.children = children
    
    def __str__(self) -> str:
        return str(self.data)

class FileNode(TreeNode):
    def __init__(self, data: str):
        super().__init__(data, None)

class FolderNode(TreeNode):
    def __init__(self, data: str):
        super().__init__(data, {})

class MetaData(TypedDict):
    name: str
    id: str

class NavigateTree():
    def __init__(self):
        self.root = FolderNode('root')
    
    def traverse(self, path: list[str]) -> FolderNode | FileNode | None: 
        try:
            destinationNode = self.root
            for step in path:
               destinationNode = destinationNode.children[step] 
            return destinationNode
        except:
            return None

    def insertFolderNode(self, path: list[str], metaData: MetaData) -> bool:
        destinationNode = self.traverse(path)
        if destinationNode is None or not isinstance(destinationNode, FolderNode):
            return False
        folderName, id = metaData['name'], metaData['id']
        destinationNode.children[folderName] = FolderNode(id)
        return True
        
    def insertFileNode(self, path: list[str], metaData: MetaData) -> bool:
        destinationNode = self.traverse(path)
        if destinationNode is None or not isinstance(destinationNode, FolderNode):
            return False
        fileName, id = metaData['name'], metaData['id']
        destinationNode.children[fileName] = FileNode(id)
        return True

    def insertMultipleFileNodeInSameFolderNode(self, path: list[str], metaDataList: list[MetaData]) -> bool:
        destinationNode = self.traverse(path)
        if destinationNode is None or not isinstance(destinationNode, FolderNode):
            return False
        for metaData in metaDataList:
            fileName, id = metaData['name'], metaData['id']
            destinationNode.children[fileName] = FileNode(id)
        return True

    def deleteFileNode(self, path: list[str], deleteFileName: str) -> bool:
        return self.deleteNode(path, deleteFileName)

    def deleteMultipleFileNodeInSameFolderNode(self, path: list[str], deleteFileNameList: list[str]) -> bool:
        return self.deleteMultipleNodeInSameFolderNode(path, deleteFileNameList)

    def deleteFolderNode(self, path: list[str], deleteFolderName: str) -> bool:
        return self.deleteNode(path, deleteFolderName)

    def deleteMultipleFolderNodeInSameFolderNode(self, path: list[str], deleteFolderNameList: list[str]) -> bool:
        return self.deleteNode(path, deleteFolderNameList)

    def deleteNode(self, path: list[str], deleteName: str) -> bool:
        destinationNode = self.traverse(path)
        if destinationNode is None or not isinstance(destinationNode, FolderNode):
            return False
        try:
            del destinationNode.children[deleteName]
        except KeyError:
            return False
        return True
        
    def deleteMultipleNodeInSameFolderNode(self, path: list[str], deleteNameList: list[str]) -> bool:
        destinationNode = self.traverse(path)
        if destinationNode is None or not isinstance(destinationNode, FolderNode):
            return False
        try:
            for deleteName in deleteNameList:
                del destinationNode.children[deleteName]
        except KeyError:
            return False
        return True



    

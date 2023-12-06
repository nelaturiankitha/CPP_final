import ast
import boto3

dyndb = boto3.resource('dynamodb')
table = dyndb.Table('call_graphs') 

class CallGraphVisitor(ast.NodeVisitor):
  def store_call_graph(file_path):
    visitor = CallGraphVisitor()
    visitor.visit(ast.parse(open(file_path).read()))
   
    graph = visitor.graph

    table.put_item(
       Item={
           'file': file_path,
           'graph': graph 
    })
    
if __name__ == '__main__':

    file_path = ''
    CallGraphVisitor.store_call_graph(file_path)
    print("Stored call graph in DynamoDB")
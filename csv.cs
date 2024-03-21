using System;
using Microsoft.VisualBasic.FileIO;

class ReadingCSV {
  public static void Main() {
    string coloumn1;
    string coloumn2;
    var path = @"D:\New folder\Data.csv";
    using (TextFieldParser csvReader = new TextFieldParser(path)) {
      csvReader.CommentTokens = new string[] { "#" };
      csvReader.SetDelimiters(new string[] { "," });
      csvReader.HasFieldsEnclosedInQuotes = true;

      // Skip the row with the column names
      csvReader.ReadLine();

      while (!csvReader.EndOfData) {
        // Read current line fields, pointer moves to the next line.
        string[] fields = csvReader.ReadFields();
        coloumn1 = fields[0];
        coloumn2 = fields[1];
      }
    }
  }
}

Public Class Form1

Dim youthAge As Integer

Private Sub InputBox_TextChanged(sender As Object, e As EventArgs) Handles InputBox.TextChanged

youthAge = Integer.Parse(InputBox.Text)

If ((youthAge >= 14) And (youthAge <= 25)) _

Then

MessageBox.Show("You are eligible to join Youth In Action!")

Else

MessageBox.Show("You are not eligible to join Youth In Action.")

End If

End Sub

Private Sub MainForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load

InputBox.Text = "Enter Your Age:"

End Sub

Private Sub SubmitButton_Click(sender As Object, e As EventArgs) Handles SubmitButton.Click

Dim name As String = NameInput.Text

Dim address As String = AddressInput.Text

Dim city As String = CityInput.Text

Dim state As String = StateInput.Text

Dim zip As Integer = Integer.Parse(ZipInput.Text)

If ((youthAge >= 14) And (youthAge <= 25)) _

Then

MessageBox.Show("You are eligible to join Youth In Action!")

End If

'Send the information to the Youth In Action server
SendToYIA(name, address, city, state, zip)

End Sub

Private Sub SendToYIA(name As String, address As String, city As String, state As String, zip As Integer)

Dim request As WebRequest = WebRequest.Create("http://www.youthinaction.org/join/")
request.Method = "POST"
Dim postData As String = String.Format("Name={0}&Address={1}&City={2}&State={3}&Zip={4}", name, address, city, state, zip)
Dim byteArray As Byte() = Encoding.UTF8.GetBytes(postData)
request.ContentType = "application/x-www-form-urlencoded"
request.ContentLength = byteArray.Length
Dim dataStream As Stream = request.GetRequestStream()
dataStream.Write(byteArray, 0, byteArray.Length)
dataStream.Close()
Dim response As WebResponse = request.GetResponse()
dataStream = response.GetResponseStream()
Dim reader As New StreamReader(dataStream)
Dim responseFromServer As String = reader.ReadToEnd()
reader.Close()
dataStream.Close()
response.Close()

End Sub

End Class
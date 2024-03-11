<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <link rel="stylesheet" type="text/css" href="iskola.css" />
    </head>
    <body>
      <h2>Tanított osztályok</h2>
      <xsl:for-each select="//osztaly">
        <table border="1">
          <tr>
            <td><xsl:value-of select="./@osztaly" /></td>
            <td><xsl:value-of select="./@ofo" /></td>
            <td><xsl:value-of select="./@tipus" /></td>
          </tr>
      </table>
        <table border="1">
          <tr>
            <th>Sorsz.</th>
            <th>OM Azon</th>
            <th>Név</th>
            <th>Megjegyzés</th>
            <th></th>
          </tr>
          <xsl:for-each select="./tanulo">
            <tr>
              <td><xsl:value-of select="./@ID" /></td>
              <td><xsl:value-of select="./@om_azon" /></td>
              <td><xsl:value-of select="./@nev" /></td>
              <td><xsl:value-of select="./@megjegyzes" /><br/><xsl:value-of select="./@koz" />
              </td>
              <td></td>
            </tr>
          </xsl:for-each>
        </table>
      </xsl:for-each>
     
    </body>
  </html>
</xsl:template>
</xsl:stylesheet>


const ListTheProduct = ({url}) => {
    console.log(url);
    
    return ( 
        <div>
            <a href={url} target="_blank" rel="noopener noreferrer">Here is the product link</a>
        </div>
     );
}
 
export default ListTheProduct;